'''
Serializacion

La finalidad de este archivo es poder 
tener los datos en formato json
'''

# Modulos
from rest_framework import serializers
from .models import Restaurante


class RestauranteSerializer(serializers.ModelSerializer):
    '''
    Clase serializadora

    Descripción:
    Esta clase es heredada de ModelSerializer, con el fin de
    poder crear un camino para serializar en el formato json
    la API la cual queremos crear
    '''
    class Meta:
        model = Restaurante
        fields = '__all__' # Denotacion para obtener los campos de la DB
