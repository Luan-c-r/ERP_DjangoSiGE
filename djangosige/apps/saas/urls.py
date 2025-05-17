from django.urls import path, re_path
from . import views

app_name = 'saas'

urlpatterns = [
    # Empresas
    path('empresas/lista/', views.EmpresaClienteListView.as_view(), name='listaempresasview'),
    path('empresas/adicionar/', views.EmpresaClienteCreateView.as_view(), name='addempresaview'),
    path('empresas/editar/<int:pk>/', views.EmpresaClienteUpdateView.as_view(), name='editarempresaview'),
    path('empresas/excluir/<int:pk>/', views.EmpresaClienteDeleteView.as_view(), name='excluirempresaview'),
    
    # Planos
    path('planos/lista/', views.PlanoListView.as_view(), name='listaplanosview'),
    path('planos/adicionar/', views.PlanoCreateView.as_view(), name='addplanoview'),
    path('planos/editar/<int:pk>/', views.PlanoUpdateView.as_view(), name='editarplanoview'),
    path('planos/excluir/<int:pk>/', views.PlanoDeleteView.as_view(), name='excluirplanoview'),
    
    # Licenças
    path('licencas/lista/', views.LicencaListView.as_view(), name='listalicencasview'),
    path('licencas/adicionar/', views.LicencaCreateView.as_view(), name='addlicencaview'),
    path('licencas/editar/<int:pk>/', views.LicencaUpdateView.as_view(), name='editarlicencaview'),
    path('licencas/excluir/<int:pk>/', views.LicencaDeleteView.as_view(), name='excluirlicencaview'),
    
    # Modelos de Empresa
    path('modelos/lista/', views.ModeloEmpresaListView.as_view(), name='listamodelosview'),
    path('modelos/adicionar/', views.ModeloEmpresaCreateView.as_view(), name='addmodeloview'),
    path('modelos/editar/<int:pk>/', views.ModeloEmpresaUpdateView.as_view(), name='editarmodeloview'),
    path('modelos/excluir/<int:pk>/', views.ModeloEmpresaDeleteView.as_view(), name='excluirmodeloview'),
    
    # Usuários de Empresa
    path('empresas/<int:empresa_id>/usuarios/', views.UsuarioEmpresaListView.as_view(), name='listausuariosempresaview'),
    path('empresas/<int:empresa_id>/usuarios/adicionar/', views.UsuarioEmpresaCreateView.as_view(), name='addusuarioempresaview'),
    path('empresas/usuarios/editar/<int:pk>/', views.UsuarioEmpresaUpdateView.as_view(), name='editarusuarioempresaview'),
    path('empresas/usuarios/excluir/<int:pk>/', views.UsuarioEmpresaDeleteView.as_view(), name='excluirusuarioempresaview'),
]
