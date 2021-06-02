from django import forms
from django.forms import ModelForm, fields, widgets
from .models import Producto

#PARA TENER FORMS CON BOOTSTRAP:
    #INSTALAR: pip install django-crispy-forms
    #AGREGAR EN INSTALLED APPS (SETTINGS): 'crispy_forms', y  CRISPY_TEMPLATE_PACK = 'bootstrap4'
    #En el template agregar : {% load crispy_forms_tags %}

class ProductoForm(ModelForm):
    nombre = forms.CharField(min_length=4,max_length=40)
    precio = forms.IntegerField(min_value=2000)
    descripcion = forms.CharField(min_length=5, max_length=60)

    class Meta:
        model = Producto
        fields = ['nombre','precio', 'imagen','descripcion','tipo', 'fecha']

        widgets = {
            'fecha': forms.SelectDateWidget(years=range(2015, 2030))
        }
