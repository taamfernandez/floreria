from django import forms
from django.forms import ModelForm
from .models import Flor

class FlorForm(ModelForm):

    nombre = forms.CharField(min_length=2, max_length=50)
    valor = forms.IntegerField(min_value=100, max_value=100000)
    descripcion = forms.CharField(min_length=10, max_length=150)
    class Meta:
        model = Flor
        fields = ['nombre', 'valor', 'descripcion', 'estado', 'stock', 'imagen']