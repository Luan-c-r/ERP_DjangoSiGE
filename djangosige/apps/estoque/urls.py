# -*- coding: utf-8 -*-

from django.urls import path, re_path
from . import views

app_name = 'estoque'
urlpatterns = [
    # Consulta de estoque
    path('consultaestoque/', views.ConsultaEstoqueView.as_view(), name='consultaestoqueview'),

    # Local de estoque
    path('local/saida/adicionar/', views.AdicionarLocalEstoqueView.as_view(), name='addlocalview'),
    path('local/listalocal/', views.LocalEstoqueListView.as_view(), name='listalocalview'),
    re_path(r'^local/editar/(?P<pk>[0-9]+)/$', views.EditarLocalEstoqueView.as_view(), name='editarlocalview'),

    # Movimento de estoque
    path('movimentos/', views.MovimentoEstoqueListView.as_view(), name='listamovimentoestoqueview'),

    # EntradaEstoque
    path('movimento/adicionarentrada/', views.AdicionarEntradaEstoqueView.as_view(), name='addentradaestoqueview'),
    path('movimento/listaentradas/', views.EntradaEstoqueListView.as_view(), name='listaentradasestoqueview'),
    re_path(r'^movimento/editarentrada/(?P<pk>[0-9]+)/$', views.DetalharEntradaEstoqueView.as_view(), name='detalharentradaestoqueview'),

    # SaidaEstoque
    path('movimento/adicionarsaida/', views.AdicionarSaidaEstoqueView.as_view(), name='addsaidaestoqueview'),
    path('movimento/listasaidas/', views.SaidaEstoqueListView.as_view(), name='listasaidasestoqueview'),
    re_path(r'^movimento/editarsaida/(?P<pk>[0-9]+)/$', views.DetalharSaidaEstoqueView.as_view(), name='detalharsaidaestoqueview'),

    # TransferenciaEstoque
    path('movimento/adicionartransferencia/', views.AdicionarTransferenciaEstoqueView.as_view(), name='addtransferenciaestoqueview'),
    path('movimento/listatransferencias/', views.TransferenciaEstoqueListView.as_view(), name='listatransferenciasestoqueview'),
    re_path(r'^movimento/editartransferencia/(?P<pk>[0-9]+)/$', views.DetalharTransferenciaEstoqueView.as_view(), name='detalhartransferenciaestoqueview'),
]
