from django.urls import path, re_path
from . import views

app_name = 'saas'

urlpatterns = [
    #Empresas
    path('saas/empresas/adicionar/', views.CadastrarEmpresaView.as_view(), name='addempresaview'),
    path('saas/empresas/lista/', views.ListaEmpresasView.as_view(), name='listaempresasview'),

    # Licenças

    # Planos

    # Acesso
]