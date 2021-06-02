from django.contrib import admin
from .models import TipoProducto, Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'descripcion', 'tipo' ]
    search_fields = ['nombre']
    list_filter = ['tipo']
    list_per_page = 10

admin.site.register(TipoProducto)
admin.site.register(Producto, ProductoAdmin)