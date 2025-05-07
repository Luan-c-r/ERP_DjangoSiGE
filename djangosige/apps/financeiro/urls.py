# -*- coding: utf-8 -*-

from django.urls import path, re_path
from . import views

app_name = 'financeiro'
urlpatterns = [
    # Lançamentos
    path('gerarlancamento/', views.GerarLancamentoView.as_view(), name='gerarlancamento'),
    path('lancamentos/', views.LancamentoListView.as_view(), name='listalancamentoview'),

    # Contas a pagar
    path('contapagar/adicionar/', views.AdicionarContaPagarView.as_view(), name='addcontapagarview'),
    path('contapagar/listacontapagar/', views.ContaPagarListView.as_view(), name='listacontapagarview'),
    re_path(r'^contapagar/editar/(?P<pk>[0-9]+)/$', views.EditarContaPagarView.as_view(), name='editarcontapagarview'),
    path('contapagar/listacontapagar/atrasadas/', views.ContaPagarAtrasadasListView.as_view(), name='listacontapagaratrasadasview'),
    path('contapagar/listacontapagar/hoje/', views.ContaPagarHojeListView.as_view(), name='listacontapagarhojeview'),

    # Contas a receber
    path('contareceber/adicionar/', views.AdicionarContaReceberView.as_view(), name='addcontareceberview'),
    path('contareceber/listacontareceber/', views.ContaReceberListView.as_view(), name='listacontareceberview'),
    re_path(r'^contareceber/editar/(?P<pk>[0-9]+)/$', views.EditarContaReceberView.as_view(), name='editarcontareceberview'),
    path('contareceber/listacontareceber/atrasadas/', views.ContaReceberAtrasadasListView.as_view(), name='listacontareceberatrasadasview'),
    path('contareceber/listacontareceber/hoje/', views.ContaReceberHojeListView.as_view(), name='listacontareceberhojeview'),

    # Pagamentos
    path('pagamento/adicionar/', views.AdicionarSaidaView.as_view(), name='addpagamentoview'),
    path('pagamento/listapagamento/', views.SaidaListView.as_view(), name='listapagamentosview'),
    re_path(r'^pagamento/editar/(?P<pk>[0-9]+)/$', views.EditarSaidaView.as_view(), name='editarpagamentoview'),

    # Recebimentos
    path('recebimento/adicionar/', views.AdicionarEntradaView.as_view(), name='addrecebimentoview'),
    path('recebimento/listarecebimento/', views.EntradaListView.as_view(), name='listarecebimentosview'),
    re_path(r'^recebimento/editar/(?P<pk>[0-9]+)/$', views.EditarEntradaView.as_view(), name='editarrecebimentoview'),

    # Faturar Pedido
    re_path(r'^faturarpedidovenda/(?P<pk>[0-9]+)/$', views.FaturarPedidoVendaView.as_view(), name='faturarpedidovenda'),
    re_path(r'^faturarpedidocompra/(?P<pk>[0-9]+)/$', views.FaturarPedidoCompraView.as_view(), name='faturarpedidocompra'),

    # Plano de contas
    path('planodecontas/', views.PlanoContasView.as_view(), name='planocontasview'),
    path('planodecontas/adicionargrupo/', views.AdicionarGrupoPlanoContasView.as_view(), name='addgrupoview'),
    re_path(r'^planodecontas/editargrupo/(?P<pk>[0-9]+)/$', views.EditarGrupoPlanoContasView.as_view(), name='editargrupoview'),

    # Fluxo de caixa
    path('fluxodecaixa/', views.FluxoCaixaView.as_view(), name='fluxodecaixaview'),
]
