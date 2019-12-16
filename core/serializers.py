from rest_framework import serializers
from .models import Flor

class FlorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flor
        fields = ['nombre', 'valor', 'descripcion', 'estado', 'stock','imagen']