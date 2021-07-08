from rest_framework import serializers
from . import models

class suscriptoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Suscriptor
        fields = ('id','nombre','correo','monto','fecha_suscripcion')
