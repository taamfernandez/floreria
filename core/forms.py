from django import forms
from django.forms import ModelForm
from .models import Flor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FlorForm(ModelForm):

    nombre = forms.CharField(min_length=2, max_length=50)
    valor = forms.IntegerField(min_value=100, max_value=100000)
    descripcion = forms.CharField(min_length=10, max_length=150)
    class Meta:
        model = Flor
        fields = ['nombre', 'valor', 'descripcion', 'estado', 'stock', 'imagen']

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']
        

