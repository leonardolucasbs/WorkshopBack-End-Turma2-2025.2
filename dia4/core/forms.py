from django import forms
from .models import Endereco
from django.forms import ModelForm

class EnderecoForm(ModelForm):
    class Meta: #metadados da classe
        model = Endereco
        fields = ['cep']
        labels = {
            'cep': 'CEP'
            }
        widgets = {
            'cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o CEP'})
        } 