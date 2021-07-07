import django
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls.conf import include
from .views import *
from django.conf import settings #IMG
from django.conf.urls.static import static #IMG
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('suscriptores',views.SuscripcionViewSet,basename='suscriptor')

urlpatterns = [
    path('',include(router.urls)),
]  

 #PARA AGREGAR IMG

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
