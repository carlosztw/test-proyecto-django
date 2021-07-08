from django import forms
from django.forms import ModelForm, fields, widgets
from .models import Producto, Contacto, Suscriptor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator
from django.forms import ValidationError

#PARA TENER FORMS CON BOOTSTRAP:
    #INSTALAR: pip install django-crispy-forms
    #AGREGAR EN INSTALLED APPS (SETTINGS): 'crispy_forms', y  CRISPY_TEMPLATE_PACK = 'bootstrap4'
    #En el template agregar : {% load crispy_forms_tags %}

class ProductoForm(ModelForm):
    nombre = forms.CharField(min_length=4,max_length=40)
    precio = forms.IntegerField(min_value=2000)
    descripcion = forms.CharField(min_length=5, max_length=60)
    imagen = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_file_size=2)])
    descuento = forms.IntegerField(min_value=0, max_value=90)
    stock =  forms.IntegerField(min_value=0)
    
    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Producto.objects.filter(nombre__iexact=nombre)

        if self.instance.pk is not None:
            existe = existe.exclude(pk=self.instance.pk)
        if existe.exists():
            raise ValidationError("Este nombre ya existe")

        return nombre    

    class Meta:
        model = Producto
        fields = ['nombre','precio', 'imagen','descripcion','tipo', 'fecha', 'descuento', 'stock']
        widgets = {
            'fecha': forms.SelectDateWidget(years=range(2015, 2030))
        }

class ContactoForm(ModelForm):    

    nombre = forms.CharField(min_length=4, max_length=60)
    class Meta:
        model = Contacto
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm): 
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class SuscripcionForm(ModelForm):
    class Meta:
        model = Suscriptor
        fields = "__all__"