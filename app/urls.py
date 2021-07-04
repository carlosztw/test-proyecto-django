import django
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import *
from django.conf import settings #IMG
from django.conf.urls.static import static #IMG



urlpatterns = [
    path('', index, name="index"),
    path('productos/', productos, name="productos"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('contacto/', contacto, name="contacto"),
    path('agregarproducto/', agregar_producto, name="agregar_producto"),
    path('modificarproducto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminarproducto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('modificar-productos/', modificar, name="modificar"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registrousuario/', registro_usuario, name="registro_usuario" )
]  

 #PARA AGREGAR IMG

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
