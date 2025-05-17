from django.contrib import admin
from .models.empresas import EmpresaCliente, Plano, Licenca, ModeloEmpresa, UsuarioEmpresa

# Registrar modelos no admin
@admin.register(EmpresaCliente)
class EmpresaClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'plano', 'licenca', 'licenca_ativa', 'data_fim_licenca')
    list_filter = ('plano', 'licenca', 'licenca_ativa', 'modelo_empresa')
    search_fields = ('nome', 'cnpj', 'email')
    date_hierarchy = 'data_cadastro'

@admin.register(Plano)
class PlanoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco_mensal', 'max_usuarios', 'permite_atribuicao_cargo', 'permite_dominio_personalizado')
    list_filter = ('permite_atribuicao_cargo', 'permite_dominio_personalizado')

@admin.register(Licenca)
class LicencaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'duracao_dias', 'multiplicador_preco')

@admin.register(ModeloEmpresa)
class ModeloEmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

@admin.register(UsuarioEmpresa)
class UsuarioEmpresaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'empresa', 'cargo', 'responsavel', 'data_vinculo')
    list_filter = ('responsavel', 'empresa')
    search_fields = ('usuario__username', 'empresa__nome', 'cargo')
