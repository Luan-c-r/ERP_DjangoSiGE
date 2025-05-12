from djangosige.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView

from djangosige.apps.cadastro.forms import PessoaJuridicaForm, PessoaFisicaForm, EnderecoFormSet, TelefoneFormSet, EmailFormSet, \
    SiteFormSet, BancoFormSet, DocumentoFormSet
from djangosige.apps.cadastro.models import PessoaFisica, PessoaJuridica, Endereco, Telefone, Email, Site, Banco, Documento

class AdicionarEmpresaView(CustomCreateView):

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, nome_razao_social=self.object.nome_razao_social)

    def get(self, request, form, *args, **kwargs):
        self.object = None

        veiculo_form = kwargs.pop('veiculo_form', None)

        pessoa_juridica_form = PessoaJuridicaForm(prefix='pessoa_jur_form')
        pessoa_fisica_form = PessoaFisicaForm(prefix='pessoa_fis_form')

        endereco_form = EnderecoFormSet(prefix='endereco_form')
        endereco_form.can_delete = False

        banco_form = BancoFormSet(prefix='banco_form')
        banco_form.can_delete = False

        documento_form = DocumentoFormSet(prefix='documento_form')
        documento_form.can_delete = False

        telefone_form = TelefoneFormSet(prefix='telefone_form')
        email_form = EmailFormSet(prefix='email_form')
        site_form = SiteFormSet(prefix='site_form')

        formsets = [telefone_form, email_form, site_form]
        for formset in formsets:
            formset.can_delete = False

        return self.render_to_response(self.get_context_data(form=form,
                                                             pessoa_juridica_form=pessoa_juridica_form,
                                                             pessoa_fisica_form=pessoa_fisica_form,
                                                             endereco_form=endereco_form,
                                                             banco_form=banco_form,
                                                             documento_form=documento_form,
                                                             formsets=formsets,
                                                             veiculo_form=veiculo_form))

    def post(self, request, form, *args, **kwargs):
        self.object = None
        extra_forms = []

        veiculo_form = kwargs.pop('veiculo_form', None)

        endereco_form = EnderecoFormSet(request.POST, prefix='endereco_form')
        banco_form = BancoFormSet(request.POST, prefix='banco_form')
        documento_form = DocumentoFormSet(
            request.POST, prefix='documento_form')

        telefone_form = TelefoneFormSet(request.POST, prefix='telefone_form')
        email_form = EmailFormSet(request.POST, prefix='email_form')
        site_form = SiteFormSet(request.POST, prefix='site_form')

        formsets = [telefone_form, email_form, site_form]

        if veiculo_form:
            extra_forms = [veiculo_form, ]

        if form.is_valid():

            self.object = form.save(commit=False)
            if self.object.tipo_pessoa == 'PJ':
                pessoa_form = PessoaJuridicaForm(
                    request.POST, prefix='pessoa_jur_form')
            else:
                pessoa_form = PessoaFisicaForm(
                    request.POST, prefix='pessoa_fis_form')

            if (all(formset.is_valid() for formset in formsets) and
                pessoa_form.is_valid() and
                endereco_form.is_valid() and
                banco_form.is_valid() and
                documento_form.is_valid() and
                    all(extra_form.is_valid() for extra_form in extra_forms)):

                self.object.save()

                # Salvar informacoes endereco
                endereco_form.instance = self.object
                end = endereco_form.save()
                if len(end):
                    self.object.endereco_padrao = end[0]

                # Salvar informacoes bancarias
                banco_form.instance = self.object
                ban = banco_form.save()
                if len(ban):
                    self.object.banco_padrao = ban[0]

                # Salvar documentos adicionais
                documento_form.instance = self.object
                documento_form.save()

                # salvar telefone
                telefone_form.instance = self.object
                tel = telefone_form.save()
                if len(tel):
                    self.object.telefone_padrao = tel[0]

                # salvar email
                email_form.instance = self.object
                ema = email_form.save()
                if len(ema):
                    self.object.email_padrao = ema[0]

                # salvar site
                site_form.instance = self.object
                sit = site_form.save()
                if len(sit):
                    self.object.site_padrao = sit[0]

                if veiculo_form:
                    veiculo_form.instance = self.object
                    veiculo_form.save()

                # salvar objeto criado e pessoa fisica/juridica
                self.object.save()
                pessoa_form.instance.pessoa_id = self.object
                pessoa_form.save()

                return self.form_valid(form)

        pessoa_juridica_form = PessoaJuridicaForm(
            request.POST, prefix='pessoa_jur_form')
        pessoa_fisica_form = PessoaFisicaForm(
            request.POST, prefix='pessoa_fis_form')

        return self.form_invalid(form=form,
                                 pessoa_juridica_form=pessoa_juridica_form,
                                 pessoa_fisica_form=pessoa_fisica_form,
                                 endereco_form=endereco_form,
                                 banco_form=banco_form,
                                 documento_form=documento_form,
                                 formsets=formsets,
                                 veiculo_form=veiculo_form)

class ListView(CustomListView):

    def __init__(self, *args, **kwargs):
        super(ListView, self).__init__(*args, **kwargs)