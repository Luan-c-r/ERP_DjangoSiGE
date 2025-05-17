from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from djangosige.apps.base.views_mixins import SuperUserRequiredMixin, FormValidationMessageMixin

class SaasListView(SuperUserRequiredMixin, ListView):
    """
    View base para listagem de objetos no app SAAS
    Restringe acesso apenas a superusuários
    """
    template_name = None
    model = None
    context_object_name = 'all_objects'
    permission_codename = None

    def get_context_data(self, **kwargs):
        context = super(SaasListView, self).get_context_data(**kwargs)
        return context

class SaasCreateView(SuperUserRequiredMixin, FormValidationMessageMixin, CreateView):
    """
    View base para criação de objetos no app SAAS
    Restringe acesso apenas a superusuários
    """
    template_name = None
    form_class = None
    model = None
    success_url = None
    success_message = "%(nome)s adicionado com sucesso."
    permission_codename = None

    def get_context_data(self, **kwargs):
        context = super(SaasCreateView, self).get_context_data(**kwargs)
        return context

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data)

class SaasUpdateView(SuperUserRequiredMixin, FormValidationMessageMixin, UpdateView):
    """
    View base para edição de objetos no app SAAS
    Restringe acesso apenas a superusuários
    """
    template_name = None
    form_class = None
    model = None
    success_url = None
    success_message = "%(nome)s editado com sucesso."
    permission_codename = None

    def get_context_data(self, **kwargs):
        context = super(SaasUpdateView, self).get_context_data(**kwargs)
        return context

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data)

class SaasDeleteView(SuperUserRequiredMixin, DeleteView):
    """
    View base para exclusão de objetos no app SAAS
    Restringe acesso apenas a superusuários
    """
    template_name = 'saas/confirm_delete.html'
    model = None
    success_url = None
    success_message = "Exclusão realizada com sucesso."
    permission_codename = None

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message)
        return super(SaasDeleteView, self).delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SaasDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Confirmar exclusão'
        return context
