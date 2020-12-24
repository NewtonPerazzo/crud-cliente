from django import forms
from app import models


class ClienteForm(forms.ModelForm):


    class Meta():
        model = models.Cliente
        fields = ('nome', 'endereco', 'telefone', 'data_nascimento')