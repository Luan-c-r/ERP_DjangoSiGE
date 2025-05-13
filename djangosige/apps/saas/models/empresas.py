from django.db import models
from django.contrib.auth.models import User  # Importe o modelo User

class EmpresaCliente(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário Responsável")
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True, verbose_name="CNPJ")
    endereco = models.TextField(verbose_name="Endereço")
    telefone = models.CharField(max_length=15, black=True, null=True, verbose_name="Telefone")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")
    plano = models.CharField(max_length=100, blank=True, null=True, verbose_name="Plano")
    licenca_ativa = models.BooleanField(default=True, verbose_name="Liceça Ativa")
    # Outros campos relacionados a Plano, Licença e Acesso

    class Meta:
        verbose_name = "Empresa Clente"
        verbose_name_plural = "Empresas Clientes"

    def __str__(self):
        return self.nome