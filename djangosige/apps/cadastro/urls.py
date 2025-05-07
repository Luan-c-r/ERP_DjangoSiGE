# -*- coding: utf-8 -*-

from django.urls import path, re_path
from . import views

app_name = 'cadastro'
urlpatterns = [
    # Empresa
    path('empresa/adicionar/', views.AdicionarEmpresaView.as_view(), name='addempresaview'),
    path('empresa/listaempresas/', views.EmpresasListView.as_view(), name='listaempresasview'),
    re_path(r'^empresa/editar/(?P<pk>[0-9]+)/$', views.EditarEmpresaView.as_view(), name='editarempresaview'),

    # Cliente
    path('cliente/adicionar/', views.AdicionarClienteView.as_view(), name='addclienteview'),
    path('cliente/listaclientes/', views.ClientesListView.as_view(), name='listaclientesview'),
    re_path(r'^cliente/editar/(?P<pk>[0-9]+)/$', views.EditarClienteView.as_view(), name='editarclienteview'),

    # Fornecedor
    path('fornecedor/adicionar/', views.AdicionarFornecedorView.as_view(), name='addfornecedorview'),
    path('fornecedor/listafornecedores/', views.FornecedoresListView.as_view(), name='listafornecedoresview'),
    re_path(r'^fornecedor/editar/(?P<pk>[0-9]+)/$', views.EditarFornecedorView.as_view(), name='editarfornecedorview'),

    # Transportadora
    path('transportadora/adicionar/', views.AdicionarTransportadoraView.as_view(), name='addtransportadoraview'),
    path('transportadora/listatransportadoras/', views.TransportadorasListView.as_view(), name='listatransportadorasview'),
    re_path(r'^transportadora/editar/(?P<pk>[0-9]+)/$', views.EditarTransportadoraView.as_view(), name='editartransportadoraview'),

    # Produto
    path('produto/adicionar/', views.AdicionarProdutoView.as_view(), name='addprodutoview'),
    path('produto/listaprodutos/', views.ProdutosListView.as_view(), name='listaprodutosview'),
    path('produto/listaprodutos/baixoestoque/', views.ProdutosBaixoEstoqueListView.as_view(), name='listaprodutosbaixoestoqueview'),
    re_path(r'^produto/editar/(?P<pk>[0-9]+)/$', views.EditarProdutoView.as_view(), name='editarprodutoview'),

    # Outros
    path('outros/adicionarcategoria/', views.AdicionarCategoriaView.as_view(), name='addcategoriaview'),
    path('outros/listacategorias/', views.CategoriasListView.as_view(), name='listacategoriasview'),
    re_path(r'^outros/editarcategoria/(?P<pk>[0-9]+)/$', views.EditarCategoriaView.as_view(), name='editarcategoriaview'),

    path('outros/adicionarunidade/', views.AdicionarUnidadeView.as_view(), name='addunidadeview'),
    path('outros/listaunidades/', views.UnidadesListView.as_view(), name='listaunidadesview'),
    re_path(r'^outros/editarunidade/(?P<pk>[0-9]+)/$', views.EditarUnidadeView.as_view(), name='editarunidadeview'),

    path('outros/adicionarmarca/', views.AdicionarMarcaView.as_view(), name='addmarcaview'),
    path('outros/listamarcas/', views.MarcasListView.as_view(), name='listamarcasview'),
    re_path(r'^outros/editarmarca/(?P<pk>[0-9]+)/$', views.EditarMarcaView.as_view(), name='editarmarcaview'),

    # Informações de empresa (Ajax request)
    path('infoempresa/', views.InfoEmpresa.as_view(), name='infoempresa'),
    path('infofornecedor/', views.InfoFornecedor.as_view(), name='infofornecedor'),
    path('infocliente/', views.InfoCliente.as_view(), name='infocliente'),
    path('infotransportadora/', views.InfoTransportadora.as_view(), name='infotransportadora'),
    path('infoproduto/', views.InfoProduto.as_view(), name='infoproduto'),
]
