from django.shortcuts import render
from django.urls import reverse_lazy
from .base import ListView, AdicionarEmpresaView

class CadastrarEmpresaView(AdicionarEmpresaView):
    template_name = 'saas/cadastrar_empresa.html'
    model = ''
    success_url = reverse_lazy('saas:addempresaview')
    success_message = "Empresa <b>%(nome_razao_social)s </b>adicionada com sucesso."
    permission_codename = 'add_empresa'

    def get_context_data(self, **kwargs):
        context = super(AdicionarEmpresaView, self).get_context_data(**kwargs)
        context['title_complete'] = 'CADASTRAR EMPRESA'
        context['return_url'] = reverse_lazy('saas:listaempresasview')
        context['tipo_pessoa'] = 'empresa'
        return context


class ListaEmpresasView(ListView):
    template_name = 'saas/lista_empresas.html'
    model = ''
    success_url = reverse_lazy('saas:listaempresasview')
    permission_codename = 'view_empresas'

    def get_context_data(self, **kwargs):
        context = super(ListaEmpresasView, self).get_context_data(**kwargs)
        context['title_complete'] = 'EMPRESAS CADASTRADAS'
        context['add_url'] = reverse_lazy('saas:addempresaview')
        context['tipo_pessoa'] = 'empresa'
        return context
    



