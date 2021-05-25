from django import forms
from django.forms import ModelForm, fields, widgets
from .models import Producto

#PARA TENER FORMS CON BOOTSTRAP:
    #INSTALAR: pip install django-crispy-forms
    #AGREGAR EN INSTALLED APPS (SETTINGS): 'crispy_forms', y  CRISPY_TEMPLATE_PACK = 'bootstrap4'
    #En el template agregar : {% load crispy_forms_tags %}

class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre','precio', 'imagen','descripcion','tipo']
