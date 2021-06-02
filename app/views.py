from django.http.response import Http404
from app.forms import ProductoForm
from django.shortcuts import render, redirect
from .models import Producto
from django.core.paginator import Page, Paginator
from django.http import Http404
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
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productoAll, 9)
        productoAll = paginator.page(page)
    except:
        raise Http404

    datos = {
        'listaProductos' : productoAll,
        'paginator': paginator
    }
    return render(request, 'app/productos.html', datos)    

def agregar_producto(request):
    datos = {
        'form' : ProductoForm()    
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(request.POST,request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto agregado correctamente a la base de datos"

    return render(request, 'app/agregar_producto.html', datos)


def modificar_producto(request, id):
    producto = Producto.objects.get(id=id)
    datos = {
        'form' : ProductoForm(instance=producto)    
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST,request.FILES,instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto modificado correctamente"
            datos['form'] = formulario

    return render(request, 'app/modificar_producto.html', datos)

def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()

    return redirect(to="modificar")    


#SEPARAR LA SECCION DE PRODUCTOS Y MODIFICAR

def modificar(request):
    productoAll = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productoAll, 9)
        productoAll = paginator.page(page)
    except:
        raise Http404    
    datos = {
        'listaProductos' : productoAll,
        'paginator': paginator
    }
    return render(request, 'app/modificar.html', datos)     
