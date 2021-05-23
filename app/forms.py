from django import forms
from django.forms import ModelForm, fields
from .models import Producto

class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre','precio', 'imagen','descripcion','tipo']