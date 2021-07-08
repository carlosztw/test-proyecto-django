from django.contrib.auth import authenticate, login
from django.http.response import Http404
from app.forms import CustomUserCreationForm, ProductoForm, ContactoForm, SuscripcionForm
from django.shortcuts import render, redirect
from .models import Producto
from django.core.paginator import Page, Paginator
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.views import APIView
from rest_framework.response import Response
from app import serializers
from app import models
from rest_framework import viewsets
from django.contrib.auth.models import Group



# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def productos(request):
    return render(request, 'app/productos.html')

def quienessomos(request):
    return render(request, 'app/quienessomos.html')

def contacto(request):
    return render(request, 'app/contacto.html')    



def contacto(request):
    datos = {
        'form': ContactoForm()
    }
    
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        datos['mensaje'] = "Solicitud enviada correctamente"    
    
    return render(request, 'app/contacto.html', datos)   


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

@permission_required('app.add_producto')
def agregar_producto(request):
    datos = {
        'form' : ProductoForm()    
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(request.POST,request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto agregado correctamente a la base de datos"
        datos["form"] = formulario

    return render(request, 'app/agregar_producto.html', datos)

@permission_required('app.change_producto')
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
        datos["form"] = formulario
    return render(request, 'app/modificar_producto.html', datos)

@permission_required('app.delete_producto')
def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()

    return redirect(to="modificar")    


#SEPARAR LA SECCION DE PRODUCTOS Y MODIFICAR
@permission_required('app.change_producto')
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

def registro_usuario(request):    
    datos = {
        'form' : CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            usuario = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, usuario)
            return redirect(to=index)
        datos["form"] = formulario   
    return render(request, 'registration/signup.html', datos)


def suscripcion(request):
    datos = {
        'form' : SuscripcionForm()
    }
    if request.method == 'POST':
        formulario = SuscripcionForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            grupo = Group.objects.get(name='Suscriptor')
            user = request.user
            user.groups.add(grupo)
            return redirect(to=index)
        datos["form"] = formulario   
    return render(request, 'app/suscripcion.html', datos)


def desuscripcion(request):
    if request.method == 'POST':
        user = request.user
        group = Group.objects.get(name='Suscriptor') 
        user.groups.remove(group)
        return render(request, 'app/index.html')
    return render(request, 'app/desuscribirse.html')






class SuscripcionViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.suscriptoresSerializer

    def get_queryset(self):
        queryset = models.Suscriptor.objects.all()
        return queryset


    def patch(self,request,pk=None):
        return Response({'method':'patch'})


    def delete(self,request,pk=None):
        return Response({'method':'delete'})

def crear_suscripcion(request):
    form = SuscripcionForm()
    return render(request, 'suscripcion.html',{'form':form})