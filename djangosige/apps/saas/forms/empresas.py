from django import forms
from ..models.empresas import EmpresaCliente, Plano, Licenca, ModeloEmpresa, UsuarioEmpresa
from django.contrib.auth.models import User
from datetime import date, timedelta

class PlanoForm(forms.ModelForm):
    class Meta:
        model = Plano
        fields = ('nome', 'descricao', 'preco_mensal', 'max_usuarios', 
                  'permite_atribuicao_cargo', 'permite_dominio_personalizado')
        widgets = {
            'nome': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'preco_mensal': forms.NumberInput(attrs={'class': 'form-control'}),
            'max_usuarios': forms.NumberInput(attrs={'class': 'form-control'}),
            'permite_atribuicao_cargo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'permite_dominio_personalizado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class LicencaForm(forms.ModelForm):
    class Meta:
        model = Licenca
        fields = ('nome', 'descricao', 'duracao_dias', 'multiplicador_preco')
        widgets = {
            'nome': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'duracao_dias': forms.NumberInput(attrs={'class': 'form-control'}),
            'multiplicador_preco': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ModeloEmpresaForm(forms.ModelForm):
    class Meta:
        model = ModeloEmpresa
        fields = ('nome', 'descricao', 'apps_disponiveis')
        widgets = {
            'nome': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'apps_disponiveis': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class EmpresaClienteForm(forms.ModelForm):
    class Meta:
        model = EmpresaCliente
        fields = ('nome', 'cnpj', 'inscricao_estadual', 'endereco', 'telefone', 'email',
                  'plano', 'licenca', 'modelo_empresa', 'dominio_personalizado', 'observacoes')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'inscricao_estadual': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'plano': forms.Select(attrs={'class': 'form-control'}),
            'licenca': forms.Select(attrs={'class': 'form-control'}),
            'modelo_empresa': forms.Select(attrs={'class': 'form-control'}),
            'dominio_personalizado': forms.TextInput(attrs={'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        plano = cleaned_data.get('plano')
        licenca = cleaned_data.get('licenca')
        dominio_personalizado = cleaned_data.get('dominio_personalizado')
        
        # Validações específicas baseadas no plano
        if plano:
            # Plano Free não deve ter licença
            if plano.nome == 'free' and licenca:
                self.add_error('licenca', 'Plano Free não requer licença.')
            
            # Planos não-Free devem ter licença
            if plano.nome != 'free' and not licenca:
                self.add_error('licenca', 'Este plano requer uma licença válida.')
            
            # Apenas plano Premium permite domínio personalizado
            if dominio_personalizado and not plano.permite_dominio_personalizado:
                self.add_error('dominio_personalizado', 'Apenas o plano Premium permite domínio personalizado.')
        
        return cleaned_data
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # Configurar datas de licença
        if instance.licenca and instance.plano.nome != 'free':
            instance.data_inicio_licenca = date.today()
            instance.data_fim_licenca = date.today() + timedelta(days=instance.licenca.duracao_dias)
            instance.licenca_ativa = True
        else:
            instance.licenca = None
            instance.data_inicio_licenca = None
            instance.data_fim_licenca = None
            
        if commit:
            instance.save()
        return instance

class UsuarioEmpresaForm(forms.ModelForm):
    class Meta:
        model = UsuarioEmpresa
        fields = ('usuario', 'empresa', 'cargo', 'responsavel')
        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'empresa': forms.Select(attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'responsavel': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        usuario = cleaned_data.get('usuario')
        empresa = cleaned_data.get('empresa')
        responsavel = cleaned_data.get('responsavel')
        
        if empresa and usuario:
            # Verificar se o plano permite mais usuários
            usuarios_existentes = UsuarioEmpresa.objects.filter(empresa=empresa).count()
            
            if usuarios_existentes >= empresa.plano.max_usuarios:
                self.add_error('usuario', f'O plano da empresa permite no máximo {empresa.plano.max_usuarios} usuários.')
            
            # Verificar se já existe um responsável caso este usuário seja marcado como responsável
            if responsavel:
                responsavel_existente = UsuarioEmpresa.objects.filter(
                    empresa=empresa, 
                    responsavel=True
                ).exclude(usuario=usuario).exists()
                
                if responsavel_existente:
                    self.add_error('responsavel', 'Esta empresa já possui um usuário responsável.')
        
        return cleaned_data
