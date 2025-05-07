# -*- coding: utf-8 -*-

from django.urls import path, re_path
from . import views

app_name = 'fiscal'
urlpatterns = [
    # Nota fiscal saída
    path('notafiscal/saida/adicionar/', views.AdicionarNotaFiscalSaidaView.as_view(), name='addnotafiscalsaidaview'),
    path('notafiscal/saida/listanotafiscal/', views.NotaFiscalSaidaListView.as_view(), name='listanotafiscalsaidaview'),
    re_path(r'^notafiscal/saida/editar/(?P<pk>[0-9]+)/$', views.EditarNotaFiscalSaidaView.as_view(), name='editarnotafiscalsaidaview'),
    path('notafiscal/saida/importar/', views.ImportarNotaSaidaView.as_view(), name='importarnotafiscalsaida'),
    re_path(r'^notafiscal/saida/gerar/(?P<pk>[0-9]+)/$', views.GerarNotaFiscalSaidaView.as_view(), name='gerarnotafiscalsaida'),

    # Nota fiscal entrada
    path('notafiscal/entrada/listanotafiscal/', views.NotaFiscalEntradaListView.as_view(), name='listanotafiscalentradaview'),
    re_path(r'^notafiscal/entrada/editar/(?P<pk>[0-9]+)/$', views.EditarNotaFiscalEntradaView.as_view(), name='editarnotafiscalentradaview'),
    path('notafiscal/entrada/importar/', views.ImportarNotaEntradaView.as_view(), name='importarnotafiscalentrada'),

    # Configuração NF-e
    path('notafiscal/configuracaonotafiscal/', views.ConfiguracaoNotaFiscalView.as_view(), name='configuracaonotafiscal'),

    # Natureza operação
    path('naturezaoperacao/adicionar/', views.AdicionarNaturezaOperacaoView.as_view(), name='addnaturezaoperacaoview'),
    path('naturezaoperacao/listanaturezaoperacao/', views.NaturezaOperacaoListView.as_view(), name='listanaturezaoperacaoview'),
    re_path(r'^naturezaoperacao/editar/(?P<pk>[0-9]+)/$', views.EditarNaturezaOperacaoView.as_view(), name='editarnaturezaoperacaoview'),

    # Grupo fiscal
    path('grupofiscal/adicionar/', views.AdicionarGrupoFiscalView.as_view(), name='addgrupofiscalview'),
    path('grupofiscal/listagrupofiscal/', views.GrupoFiscalListView.as_view(), name='listagrupofiscalview'),
    re_path(r'^grupofiscal/editar/(?P<pk>[0-9]+)/$', views.EditarGrupoFiscalView.as_view(), name='editargrupofiscalview'),

    # Ações Nota Fiscal
    re_path(r'^notafiscal/validar/(?P<pk>[0-9]+)/$', views.ValidarNotaView.as_view(), name='validarnotafiscal'),
    re_path(r'^notafiscal/emitir/(?P<pk>[0-9]+)/$', views.EmitirNotaView.as_view(), name='emitirnotafiscal'),
    re_path(r'^notafiscal/copiar/(?P<pk>[0-9]+)/$', views.GerarCopiaNotaView.as_view(), name='copiarnotafiscal'),
    re_path(r'^notafiscal/cancelar/(?P<pk>[0-9]+)/$', views.CancelarNotaView.as_view(), name='cancelarnotafiscal'),
    re_path(r'^notafiscal/gerardanfe/(?P<pk>[0-9]+)/$', views.GerarDanfeView.as_view(), name='gerardanfe'),
    re_path(r'^notafiscal/gerardanfce/(?P<pk>[0-9]+)/$', views.GerarDanfceView.as_view(), name='gerardanfce'),

    # Comunicação SEFAZ
    path('notafiscal/consultarcadastro/', views.ConsultarCadastroView.as_view(), name='consultarcadastro'),
    path('notafiscal/inutilizarnotas/', views.InutilizarNotasView.as_view(), name='inutilizarnotas'),
    path('notafiscal/consultarnota/', views.ConsultarNotaView.as_view(), name='consultarnota'),
    re_path(r'^notafiscal/consultarnota/(?P<pk>[0-9]+)/$', views.ConsultarNotaView.as_view(), name='consultarnota'),
    path('notafiscal/baixarnota/', views.BaixarNotaView.as_view(), name='baixarnota'),
    re_path(r'^notafiscal/baixarnota/(?P<pk>[0-9]+)/$', views.BaixarNotaView.as_view(), name='baixarnota'),
    path('notafiscal/manifestacaodestinatario/', views.ManifestacaoDestinatarioView.as_view(), name='manifestacaodestinatario'),
]
