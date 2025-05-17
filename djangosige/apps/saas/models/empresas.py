from django.db import models
from django.contrib.auth.models import User

class Plano(models.Model):
    """
    Modelo para os planos disponíveis no sistema
    """
    TIPO_PLANO_CHOICES = (
        ('free', 'Free'),
        ('padrao', 'Padrão'),
        ('premium', 'Premium'),
    )
    
    nome = models.CharField(max_length=100, choices=TIPO_PLANO_CHOICES)
    descricao = models.TextField(verbose_name="Descrição")
    preco_mensal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço Mensal")
    max_usuarios = models.IntegerField(verbose_name="Máximo de Usuários")
    permite_atribuicao_cargo = models.BooleanField(default=False, verbose_name="Permite Atribuição de Cargo")
    permite_dominio_personalizado = models.BooleanField(default=False, verbose_name="Permite Domínio Personalizado")
    
    class Meta:
        verbose_name = "Plano"
        verbose_name_plural = "Planos"
        
    def __str__(self):
        return self.get_nome_display()

class Licenca(models.Model):
    """
    Modelo para as licenças disponíveis no sistema
    """
    TIPO_LICENCA_CHOICES = (
        ('teste', 'Teste (30 dias)'),
        ('mensal', 'Mensal'),
        ('trimestral', 'Trimestral'),
        ('semestral', 'Semestral'),
        ('anual', 'Anual'),
    )
    
    nome = models.CharField(max_length=100, choices=TIPO_LICENCA_CHOICES)
    descricao = models.TextField(verbose_name="Descrição")
    duracao_dias = models.IntegerField(verbose_name="Duração em Dias")
    multiplicador_preco = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Multiplicador de Preço")
    
    class Meta:
        verbose_name = "Licença"
        verbose_name_plural = "Licenças"
        
    def __str__(self):
        return self.get_nome_display()

class ModeloEmpresa(models.Model):
    """
    Modelo para os tipos/ramos de empresa
    """
    TIPO_MODELO_CHOICES = (
        ('otica', 'Ótica'),
        ('joalheria', 'Joalheria'),
        ('logistica', 'Logística'),
    )
    
    nome = models.CharField(max_length=100, choices=TIPO_MODELO_CHOICES)
    descricao = models.TextField(verbose_name="Descrição")
    apps_disponiveis = models.TextField(verbose_name="Apps Disponíveis")
    
    class Meta:
        verbose_name = "Modelo de Empresa"
        verbose_name_plural = "Modelos de Empresa"
        
    def __str__(self):
        return self.get_nome_display()

class EmpresaCliente(models.Model):
    """
    Modelo para as empresas clientes
    """
    nome = models.CharField(max_length=255, verbose_name="Nome/Razão Social")
    cnpj = models.CharField(max_length=18, unique=True, verbose_name="CNPJ")
    inscricao_estadual = models.CharField(max_length=30, blank=True, null=True, verbose_name="Inscrição Estadual")
    endereco = models.TextField(verbose_name="Endereço")
    telefone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Telefone")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")
    
    # Campos relacionados a Plano, Licença e Acesso
    plano = models.ForeignKey(Plano, on_delete=models.PROTECT, verbose_name="Plano")
    licenca = models.ForeignKey(Licenca, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Licença")
    modelo_empresa = models.ForeignKey(ModeloEmpresa, on_delete=models.PROTECT, verbose_name="Modelo/Ramo da Empresa")
    
    # Campos de controle de licença
    data_inicio_licenca = models.DateField(null=True, blank=True, verbose_name="Data de Início da Licença")
    data_fim_licenca = models.DateField(null=True, blank=True, verbose_name="Data de Fim da Licença")
    licenca_ativa = models.BooleanField(default=True, verbose_name="Licença Ativa")
    
    # Campos adicionais
    dominio_personalizado = models.CharField(max_length=255, blank=True, null=True, verbose_name="Domínio Personalizado")
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")
    
    class Meta:
        verbose_name = "Empresa Cliente"
        verbose_name_plural = "Empresas Clientes"
        
    def __str__(self):
        return self.nome
    
    def calcular_preco_licenca(self):
        """
        Calcula o preço da licença baseado no plano e tipo de licença
        """
        if self.plano.nome == 'free' or not self.licenca:
            return 0
        
        return self.plano.preco_mensal * self.licenca.multiplicador_preco
    
    def verificar_licenca_valida(self):
        """
        Verifica se a licença está válida
        """
        from datetime import date
        
        # Plano free não precisa de licença
        if self.plano.nome == 'free':
            return True
            
        # Se não tiver licença ou data de fim, não é válida
        if not self.licenca or not self.data_fim_licenca:
            return False
            
        # Verifica se a data atual está dentro do período da licença
        hoje = date.today()
        return hoje <= self.data_fim_licenca and self.licenca_ativa

class UsuarioEmpresa(models.Model):
    """
    Modelo para relacionar usuários às empresas clientes
    """
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    empresa = models.ForeignKey(EmpresaCliente, on_delete=models.CASCADE, verbose_name="Empresa")
    cargo = models.CharField(max_length=100, blank=True, null=True, verbose_name="Cargo")
    responsavel = models.BooleanField(default=False, verbose_name="Responsável")
    data_vinculo = models.DateTimeField(auto_now_add=True, verbose_name="Data de Vínculo")
    
    class Meta:
        verbose_name = "Usuário da Empresa"
        verbose_name_plural = "Usuários da Empresa"
        unique_together = ('usuario', 'empresa')
        
    def __str__(self):
        return f"{self.usuario.username} - {self.empresa.nome}"
