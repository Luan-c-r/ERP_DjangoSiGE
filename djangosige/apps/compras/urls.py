# -*- coding: utf-8 -*-

from django.urls import path, re_path
from . import views

app_name = 'compras'
urlpatterns = [
    # Orcamentos de compra
    path('orcamentocompra/adicionar/', views.AdicionarOrcamentoCompraView.as_view(), name='addorcamentocompraview'),
    path('orcamentocompra/listaorcamentocompra/', views.OrcamentoCompraListView.as_view(), name='listaorcamentocompraview'),
    re_path(r'^orcamentocompra/editar/(?P<pk>[0-9]+)/$', views.EditarOrcamentoCompraView.as_view(), name='editarorcamentocompraview'),
    path('orcamentocompra/listaorcamentocompra/vencidos/', views.OrcamentoCompraVencidosListView.as_view(), name='listaorcamentocompravencidosview'),
    path('orcamentocompra/listaorcamentocompra/hoje/', views.OrcamentoCompraVencimentoHojeListView.as_view(), name='listaorcamentocomprahojeview'),

    # Pedidos de compra
    path('pedidocompra/adicionar/', views.AdicionarPedidoCompraView.as_view(), name='addpedidocompraview'),
    path('pedidocompra/listapedidocompra/', views.PedidoCompraListView.as_view(), name='listapedidocompraview'),
    re_path(r'^pedidocompra/editar/(?P<pk>[0-9]+)/$', views.EditarPedidoCompraView.as_view(), name='editarpedidocompraview'),
    path('pedidocompra/listapedidocompra/atrasados/', views.PedidoCompraAtrasadosListView.as_view(), name='listapedidocompraatrasadosview'),
    path('pedidocompra/listapedidocompra/hoje/', views.PedidoCompraEntregaHojeListView.as_view(), name='listapedidocomprahojeview'),

    # Request ajax
    path('infocompra/', views.InfoCompra.as_view(), name='infocompra'),

    # Gerar pdf orcamento
    re_path(r'^gerarpdforcamentocompra/(?P<pk>[0-9]+)/$', views.GerarPDFOrcamentoCompra.as_view(), name='gerarpdforcamentocompra'),
    # Gerar pdf pedido
    re_path(r'^gerarpdfpedidocompra/(?P<pk>[0-9]+)/$', views.GerarPDFPedidoCompra.as_view(), name='gerarpdfpedidocompra'),
    # Gerar pedido a partir de um orçamento
    re_path(r'^gerarpedidocompra/(?P<pk>[0-9]+)/$', views.GerarPedidoCompraView.as_view(), name='gerarpedidocompra'),
    # Copiar orcamento cancelado ou realizado
    re_path(r'^copiarorcamentocompra/(?P<pk>[0-9]+)/$', views.GerarCopiaOrcamentoCompraView.as_view(), name='copiarorcamentocompra'),
    # Copiar pedido cancelado ou realizado
    re_path(r'^copiarpedidocompra/(?P<pk>[0-9]+)/$', views.GerarCopiaPedidoCompraView.as_view(), name='copiarpedidocompra'),
    # Cancelar Pedido de compra
    re_path(r'^cancelarpedidocompra/(?P<pk>[0-9]+)/$', views.CancelarPedidoCompraView.as_view(), name='cancelarpedidocompra'),
    # Cancelar Orcamento de compra
    re_path(r'^cancelarorcamentocompra/(?P<pk>[0-9]+)/$', views.CancelarOrcamentoCompraView.as_view(), name='cancelarorcamentocompra'),
    # Receber Pedido de compra
    re_path(r'^receberpedidocompra/(?P<pk>[0-9]+)/$', views.ReceberPedidoCompraView.as_view(), name='receberpedidocompra'),
]
