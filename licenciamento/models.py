from django.db import models
import uuid
from django.utils import timezone
# from django.conf import settings # Para User, se necessário no futuro

class TipoNegocioCliente(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome do Tipo de Negócio")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    template_dashboard_slug = models.SlugField(max_length=100, blank=True, null=True, verbose_name="Slug do Template da Dashboard")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo de Negócio do Cliente"
        verbose_name_plural = "Tipos de Negócio dos Clientes"

class ClienteLicenciado(models.Model):
    razao_social = models.CharField(max_length=255, verbose_name="Razão Social")
    nome_fantasia = models.CharField(max_length=255, blank=True, null=True, verbose_name="Nome Fantasia")
    cnpj_cpf = models.CharField(max_length=20, unique=True, verbose_name="CNPJ/CPF")
    email_principal = models.EmailField(verbose_name="Email Principal")
    telefone_principal = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefone Principal")
    endereco = models.TextField(blank=True, null=True, verbose_name="Endereço")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")
    ativo = models.BooleanField(default=True, verbose_name="Ativo")
    tipo_negocio = models.ForeignKey(TipoNegocioCliente, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Tipo de Negócio")
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")

    # admin_cliente_user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='empresa_licenciada_admin')

    def __str__(self):
        return self.razao_social

    class Meta:
        verbose_name = "Cliente Licenciado"
        verbose_name_plural = "Clientes Licenciados"

class PlanoLicenca(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome do Plano")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    # limite_usuarios = models.PositiveIntegerField(default=1)
    # modulos_inclusos = models.ManyToManyField('ModuloSistema', blank=True) # Requereria um modelo ModuloSistema
    valor_mensal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valor_anual = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Plano de Licença"
        verbose_name_plural = "Planos de Licença"

class Licenca(models.Model):
    STATUS_CHOICES = (
        ("ativa", "Ativa"),
        ("inativa", "Inativa"),
        ("expirada", "Expirada"),
        ("suspensa", "Suspensa"),
        ("pendente", "Pendente"),
    )

    cliente = models.ForeignKey(ClienteLicenciado, on_delete=models.CASCADE, related_name='licencas', verbose_name="Cliente")
    plano = models.ForeignKey(PlanoLicenca, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Plano")
    chave_licenca = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name="Chave de Licença")
    data_emissao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Emissão")
    data_inicio_validade = models.DateField(verbose_name="Início da Validade")
    data_fim_validade = models.DateField(verbose_name="Fim da Validade")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pendente", verbose_name="Status")
    numero_max_usuarios = models.PositiveIntegerField(default=1, verbose_name="Número Máximo de Usuários")
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")

    def is_valida(self):
        hoje = timezone.now().date()
        return self.status == "ativa" and self.data_inicio_validade <= hoje <= self.data_fim_validade

    def __str__(self):
        return f"Licença {self.chave_licenca} para {self.cliente.razao_social}"

    class Meta:
        verbose_name = "Licença"
        verbose_name_plural = "Licenças"
        ordering = ["-data_emissao"]

class WidgetDashboard(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Widget")
    slug = models.SlugField(unique=True, help_text="Identificador único para o widget, usado no template.")
    template_path = models.CharField(max_length=255, help_text="Caminho para o template do widget (ex: 'widgets/vendas_dia.html')")
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class LayoutDashboard(models.Model):
    tipo_negocio = models.OneToOneField(TipoNegocioCliente, on_delete=models.CASCADE, related_name="layout_dashboard")
    nome_layout = models.CharField(max_length=100, default="Padrão")
    configuracao_widgets = models.JSONField(default=list, blank=True, help_text="Lista de slugs de widgets e suas configurações (ex: [{'slug': 'vendas_mes', 'coluna': 1, 'ordem': 1}])")

    def __str__(self):
        return f"Layout para {self.tipo_negocio.nome}"

