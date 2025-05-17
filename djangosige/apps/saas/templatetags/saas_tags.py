from django import template
from django.contrib.auth.models import User
from djangosige.apps.saas.models.empresas import UsuarioEmpresa, EmpresaCliente

register = template.Library()

@register.filter
def pertence_a_empresa(user, empresa_id):
    """
    Verifica se o usuário pertence a uma determinada empresa
    """
    if user.is_superuser:
        return True
    
    try:
        return UsuarioEmpresa.objects.filter(
            usuario=user,
            empresa_id=empresa_id
        ).exists()
    except:
        return False

@register.filter
def empresas_do_usuario(user):
    """
    Retorna as empresas às quais o usuário está vinculado
    """
    if user.is_superuser:
        return EmpresaCliente.objects.all()
    
    try:
        vinculos = UsuarioEmpresa.objects.filter(usuario=user)
        return [vinculo.empresa for vinculo in vinculos]
    except:
        return []

@register.filter
def is_responsavel(user, empresa_id):
    """
    Verifica se o usuário é responsável por uma determinada empresa
    """
    if user.is_superuser:
        return True
    
    try:
        return UsuarioEmpresa.objects.filter(
            usuario=user,
            empresa_id=empresa_id,
            responsavel=True
        ).exists()
    except:
        return False

@register.filter
def plano_permite_atribuicao_cargo(empresa_id):
    """
    Verifica se o plano da empresa permite atribuição de cargo
    """
    try:
        empresa = EmpresaCliente.objects.get(id=empresa_id)
        return empresa.plano.permite_atribuicao_cargo
    except:
        return False

@register.filter
def plano_permite_dominio_personalizado(empresa_id):
    """
    Verifica se o plano da empresa permite domínio personalizado
    """
    try:
        empresa = EmpresaCliente.objects.get(id=empresa_id)
        return empresa.plano.permite_dominio_personalizado
    except:
        return False
