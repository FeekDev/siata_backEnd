# la finalidad de este archivo es poder tener los datos en formato json

# Modulo
from rest_framework import serializers
from .models import Restaurante


class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = '__all__'
