from django.contrib import admin
from django.urls import path
from .views import index, productos, quienessomos
from django.conf import settings #IMG
from django.conf.urls.static import static #IMG

urlpatterns = [
    path('', index, name="index"),
    path('productos/', productos, name="productos"),
    path('quienessomos/', quienessomos, name="quienessomos"),
] 

 #PARA AGREGAR IMG

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
