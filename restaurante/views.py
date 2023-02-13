'''
Vistas
------
Se determina que lógica desarrollaremos para poder
responder la solicitud que se está haciendo desde cada
una de las rutas definidas
'''

# Modulos
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Restaurante
from .serializers import RestauranteSerializer

# Vistas
def index(request):
    '''
    Página de inicio
    ---------------
    En este caso tiene un mensaje sencillo
    pero podemos crear un template en HTML
    '''
    return HttpResponse("Hello, this is the home page")


@api_view(['GET', 'POST'])
def api_pagos(request):
    '''
    API general
    -----------
    Podemos listar todos los pagos
    o también realizar hacer un nuevo pago
    '''
    if request.method == 'GET':
        restaurantes = Restaurante.objects.all()
        serializer = RestauranteSerializer(restaurantes, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = RestauranteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)