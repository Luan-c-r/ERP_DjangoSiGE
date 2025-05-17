from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import transaction
from django.http import HttpResponse
from django.contrib.auth.models import User

from ..views.base import SaasListView, SaasCreateView, SaasUpdateView, SaasDeleteView
from ..models.empresas import EmpresaCliente, Plano, Licenca, ModeloEmpresa, UsuarioEmpresa
from ..forms.empresas import EmpresaClienteForm, PlanoForm, LicencaForm, ModeloEmpresaForm, UsuarioEmpresaForm

# Views para EmpresaCliente
class EmpresaClienteListView(SaasListView):
    template_name = 'saas/empresa/lista_empresas.html'
    model = EmpresaCliente
    context_object_name = 'all_empresas'
    
    def get_context_data(self, **kwargs):
        context = super(EmpresaClienteListView, self).get_context_data(**kwargs)
        context['title_complete'] = 'EMPRESAS CLIENTES'
        context['add_url'] = reverse_lazy('saas:addempresaview')
        return context

class EmpresaClienteCreateView(SaasCreateView):
    template_name = 'saas/empresa/cadastrar_empresa.html'
    form_class = EmpresaClienteForm
    model = EmpresaCliente
    success_url = reverse_lazy('saas:listaempresasview')
    success_message = "Empresa <b>%(nome)s</b> adicionada com sucesso."
    
    def get_context_data(self, **kwargs):
        context = super(EmpresaClienteCreateView, self).get_context_data(**kwargs)
        context['title_complete'] = 'CADASTRAR EMPRESA CLIENTE'
        context['return_url'] = reverse_lazy('saas:listaempresasview')
        return context

class EmpresaClienteUpdateView(SaasUpdateView):
    template_name = 'saas/empresa/editar_empresa.html'
    form_class = EmpresaClienteForm
    model = EmpresaCliente
    success_url = reverse_lazy('saas:listaempresasview')
    success_message = "Empresa <b>%(nome)s</b> editada com sucesso."
    
    def get_context_data(self, **kwargs):
        context = super(EmpresaClienteUpdateView, self).get_context_data(**kwargs)
        context['title_complete'] = 'EDITAR EMPRESA CLIENTE'
        context['return_url'] = reverse_lazy('saas:listaempresasview')
        return context

class EmpresaClienteDeleteView(SaasDeleteView):
    model = EmpresaCliente
    success_url = reverse_lazy('saas:listaempresasview')
    success_message = "Empresa excluída com sucesso."

# Views para Plano
class PlanoListView(SaasListView):
    template_name = 'saas/plano/lista_planos.html'
    model = Plano
    context_object_name = 'all_planos'
    
    def get_context_data(self, **kwargs):
        context = super(PlanoListView, self).get_context_data(**kwargs)
        context['title_complete'] = 'PLANOS DISPONÍVEIS'
        context['add_url'] = reverse_lazy('saas:addplanoview')
        return context

class PlanoCreateView(SaasCreateView):
    template_name = 'saas/plano/cadastrar_plano.html'
    form_class = PlanoForm
    model = Plano
    success_url = reverse_lazy('saas:listaplanosview')
    success_message = "Plano <b>%(nome)s</b> adicionado com sucesso."
    
    def get_context_data(self, **kwargs):
        context = super(PlanoCreateView, self).get_context_data(**kwargs)
        context['title_complete'] = 'CADASTRAR PLANO'
        context['return_url'] = reverse_lazy('saas:listaplanosview')
        return context

class PlanoUpdateView(SaasUpdateView):
    template_name = 'saas/plano/editar_plano.html'
    form_class = PlanoForm
    model = Plano
    success_url = reverse_lazy('saas:listaplanosview')
    success_message = "Plano <b>%(nome)s</b> editado com sucesso."
    
    def get_context_data(self, **kwargs):
        context = super(PlanoUpdateView, self).get_context_data(**kwargs)
        context['title_complete'] = 'EDITAR PLANO'
        context['return_url'] = reverse_lazy('saas:listaplanosview')
        return context

class PlanoDeleteView(SaasDeleteView):
    model = Plano
    success_url = reverse_lazy('saas:listaplanosview')
    success_message = "Plano excluído com sucesso."

# Views para Licença
class LicencaListView(SaasListView):
    template_name = 'saas/licenca/lista_licencas.html'
    model = Licenca
    context_object_name = 'all_licencas'
    
    def get_context_data(self, **kwargs):
        context = super(LicencaListView, self).get_context_data(**kwargs)
        context['title_complete'] = 'LICENÇAS DISPONÍVEIS'
        context['add_url'] = reverse_lazy('saas:addlicencaview')
        return context

class LicencaCreateView(SaasCreateView):
    template_name = 'saas/licenca/cadastrar_licenca.html'
    form_class = LicencaForm
    model = Licenca
    success_url = reverse_lazy('saas:listalicencasview')
    success_message = "Licença <b>%(nome)s</b> adicionada com sucesso."
    
    def get_context_data(self, **kwargs):
        context = super(LicencaCreateView, self).get_context_data(**kwargs)
        context['title_complete'] = 'CADASTRAR LICENÇA'
        context['return_url'] = reverse_lazy('saas:listalicencasview')
        return context

class LicencaUpdateView(SaasUpdateView):
    template_name = 'saas/licenca/editar_licenca.html'
    form_class = LicencaForm
    model = Licenca
    success_url = reverse_lazy('saas:listalicencasview')
    success_message = "Licença <b>%(nome)s</b> editada com sucesso."
    
    def get_context_data(self, **kwargs):
        context = super(LicencaUpdateView, self).get_context_data(**kwargs)
        context['title_complete'] = 'EDITAR LICENÇA'
        context['return_url'] = reverse_lazy('saas:listalicencasview')
        return context

class LicencaDeleteView(SaasDeleteView):
    model = Licenca
    success_url = reverse_lazy('saas:listalicencasview')
    success_message = "Licença excluída com sucesso."

# Views para ModeloEmpresa
class ModeloEmpresaListView(SaasListView):
    template_name = 'saas/modelo/lista_modelos.html'
    model = ModeloEmpresa
    context_object_name = 'all_modelos'
    
    def get_context_data(self, **kwargs):
        context = super(ModeloEmpresaListView, self).get_context_data(**kwargs)
        context['title_complete'] = 'MODELOS DE EMPRESA'
        context['add_url'] = reverse_lazy('saas:addmodeloview')
        return context

class ModeloEmpresaCreateView(SaasCreateView):
    template_name = 'saas/modelo/cadastrar_modelo.html'
    form_class = ModeloEmpresaForm
    model = ModeloEmpresa
    success_url = reverse_lazy('saas:listamodelosview')
    success_message = "Modelo <b>%(nome)s</b> adicionado com sucesso."
    
    def get_context_data(self, **kwargs):
        context = super(ModeloEmpresaCreateView, self).get_context_data(**kwargs)
        context['title_complete'] = 'CADASTRAR MODELO DE EMPRESA'
        context['return_url'] = reverse_lazy('saas:listamodelosview')
        return context

class ModeloEmpresaUpdateView(SaasUpdateView):
    template_name = 'saas/modelo/editar_modelo.html'
    form_class = ModeloEmpresaForm
    model = ModeloEmpresa
    success_url = reverse_lazy('saas:listamodelosview')
    success_message = "Modelo <b>%(nome)s</b> editado com sucesso."
    
    def get_context_data(self, **kwargs):
        context = super(ModeloEmpresaUpdateView, self).get_context_data(**kwargs)
        context['title_complete'] = 'EDITAR MODELO DE EMPRESA'
        context['return_url'] = reverse_lazy('saas:listamodelosview')
        return context

class ModeloEmpresaDeleteView(SaasDeleteView):
    model = ModeloEmpresa
    success_url = reverse_lazy('saas:listamodelosview')
    success_message = "Modelo excluído com sucesso."

# Views para UsuarioEmpresa
class UsuarioEmpresaListView(SaasListView):
    template_name = 'saas/usuario/lista_usuarios_empresa.html'
    model = UsuarioEmpresa
    context_object_name = 'all_usuarios'
    
    def get_queryset(self):
        empresa_id = self.kwargs.get('empresa_id')
        return UsuarioEmpresa.objects.filter(empresa_id=empresa_id)
    
    def get_context_data(self, **kwargs):
        context = super(UsuarioEmpresaListView, self).get_context_data(**kwargs)
        empresa = get_object_or_404(EmpresaCliente, id=self.kwargs.get('empresa_id'))
        context['title_complete'] = f'USUÁRIOS DA EMPRESA {empresa.nome.upper()}'
        context['add_url'] = reverse_lazy('saas:addusuarioempresaview', kwargs={'empresa_id': empresa.id})
        context['return_url'] = reverse_lazy('saas:listaempresasview')
        context['empresa'] = empresa
        return context

class UsuarioEmpresaCreateView(SaasCreateView):
    template_name = 'saas/usuario/cadastrar_usuario_empresa.html'
    form_class = UsuarioEmpresaForm
    model = UsuarioEmpresa
    
    def get_success_url(self):
        return reverse_lazy('saas:listausuariosempresaview', kwargs={'empresa_id': self.kwargs.get('empresa_id')})
    
    def get_form(self, form_class=None):
        form = super(UsuarioEmpresaCreateView, self).get_form(form_class)
        empresa = get_object_or_404(EmpresaCliente, id=self.kwargs.get('empresa_id'))
        form.fields['empresa'].initial = empresa
        form.fields['empresa'].widget.attrs['readonly'] = True
        return form
    
    def get_context_data(self, **kwargs):
        context = super(UsuarioEmpresaCreateView, self).get_context_data(**kwargs)
        empresa = get_object_or_404(EmpresaCliente, id=self.kwargs.get('empresa_id'))
        context['title_complete'] = f'ADICIONAR USUÁRIO À EMPRESA {empresa.nome.upper()}'
        context['return_url'] = self.get_success_url()
        context['empresa'] = empresa
        return context

class UsuarioEmpresaUpdateView(SaasUpdateView):
    template_name = 'saas/usuario/editar_usuario_empresa.html'
    form_class = UsuarioEmpresaForm
    model = UsuarioEmpresa
    
    def get_success_url(self):
        return reverse_lazy('saas:listausuariosempresaview', kwargs={'empresa_id': self.object.empresa.id})
    
    def get_context_data(self, **kwargs):
        context = super(UsuarioEmpresaUpdateView, self).get_context_data(**kwargs)
        context['title_complete'] = f'EDITAR USUÁRIO DA EMPRESA {self.object.empresa.nome.upper()}'
        context['return_url'] = self.get_success_url()
        context['empresa'] = self.object.empresa
        return context

class UsuarioEmpresaDeleteView(SaasDeleteView):
    model = UsuarioEmpresa
    
    def get_success_url(self):
        return reverse_lazy('saas:listausuariosempresaview', kwargs={'empresa_id': self.object.empresa.id})
