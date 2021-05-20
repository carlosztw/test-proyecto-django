from django.shortcuts import render
from .models import Producto
# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def productos(request):
    return render(request, 'app/productos.html')

def quienessomos(request):
    return render(request, 'app/quienessomos.html')

def productos(request):
    # CREAMOS UNA VARIABLE QUE LEE ALL EN LA BD (SELECT * FROM PRODUCTO) 
    productoAll = Producto.objects.all()
    datos = {
        'listaProductos' : productoAll
    }
    return render(request, 'app/productos.html', datos)    