from django.contrib import admin
from .models import TipoProducto, Producto, Contacto
from .forms import ProductoForm
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'descripcion', 'tipo' ]
    search_fields = ['nombre']
    list_filter = ['tipo']
    list_per_page = 10
    form = ProductoForm
admin.site.register(TipoProducto)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)