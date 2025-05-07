# -*- coding: utf-8 -*-

from django.urls import path, re_path
from . import views

app_name = 'vendas'
urlpatterns = [
    # Orcamentos de venda
    path('orcamentovenda/adicionar/', views.AdicionarOrcamentoVendaView.as_view(), name='addorcamentovendaview'),
    path('orcamentovenda/listaorcamentovenda/', views.OrcamentoVendaListView.as_view(), name='listaorcamentovendaview'),
    re_path(r'^orcamentovenda/editar/(?P<pk>[0-9]+)/$', views.EditarOrcamentoVendaView.as_view(), name='editarorcamentovendaview'),
    path('orcamentovenda/listaorcamentovenda/vencidos/', views.OrcamentoVendaVencidosListView.as_view(), name='listaorcamentovendavencidoview'),
    path('orcamentovenda/listaorcamentovenda/hoje/', views.OrcamentoVendaVencimentoHojeListView.as_view(), name='listaorcamentovendahojeview'),

    # Pedidos de venda
    path('pedidovenda/adicionar/', views.AdicionarPedidoVendaView.as_view(), name='addpedidovendaview'),
    path('pedidovenda/listapedidovenda/', views.PedidoVendaListView.as_view(), name='listapedidovendaview'),
    re_path(r'^pedidovenda/editar/(?P<pk>[0-9]+)/$', views.EditarPedidoVendaView.as_view(), name='editarpedidovendaview'),
    path('pedidovenda/listapedidovenda/atrasados/', views.PedidoVendaAtrasadosListView.as_view(), name='listapedidovendaatrasadosview'),
    path('pedidovenda/listapedidovenda/hoje/', views.PedidoVendaEntregaHojeListView.as_view(), name='listapedidovendahojeview'),

    # Condicao pagamento
    path('pagamento/adicionar/', views.AdicionarCondicaoPagamentoView.as_view(), name='addcondicaopagamentoview'),
    path('pagamento/listacondicaopagamento/', views.CondicaoPagamentoListView.as_view(), name='listacondicaopagamentoview'),
    re_path(r'^pagamento/editar/(?P<pk>[0-9]+)/$', views.EditarCondicaoPagamentoView.as_view(), name='editarcondicaopagamentoview'),

    # Request ajax views
    path('infocondpagamento/', views.InfoCondicaoPagamento.as_view(), name='infocondpagamento'),
    path('infovenda/', views.InfoVenda.as_view(), name='infovenda'),

    # Gerar pdf orcamento
    re_path(r'^gerarpdforcamentovenda/(?P<pk>[0-9]+)/$', views.GerarPDFOrcamentoVenda.as_view(), name='gerarpdforcamentovenda'),
    # Gerar pdf pedido
    re_path(r'^gerarpdfpedidovenda/(?P<pk>[0-9]+)/$', views.GerarPDFPedidoVenda.as_view(), name='gerarpdfpedidovenda'),
    # Gerar pedido a partir de um orçamento
    re_path(r'^gerarpedidovenda/(?P<pk>[0-9]+)/$', views.GerarPedidoVendaView.as_view(), name='gerarpedidovenda'),
    # Copiar orcamento cancelado ou baixado
    re_path(r'^copiarorcamentovenda/(?P<pk>[0-9]+)/$', views.GerarCopiaOrcamentoVendaView.as_view(), name='copiarorcamentovenda'),
    # Copiar pedido cancelado ou baixado
    re_path(r'^copiarpedidovenda/(?P<pk>[0-9]+)/$', views.GerarCopiaPedidoVendaView.as_view(), name='copiarpedidovenda'),
    # Cancelar Orcamento de venda
    re_path(r'^cancelarorcamentovenda/(?P<pk>[0-9]+)/$', views.CancelarOrcamentoVendaView.as_view(), name='cancelarorcamentovenda'),
    # Cancelar Pedido de venda
    re_path(r'^cancelarpedidovenda/(?P<pk>[0-9]+)/$', views.CancelarPedidoVendaView.as_view(), name='cancelarpedidovenda'),
]
