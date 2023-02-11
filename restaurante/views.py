# Modulos
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Restaurante
from .serializers import RestauranteSerializer

# Views

def index(request):
    return HttpResponse("Hello, this is the home page")


@api_view(['GET', 'POST'])
def api_pagos(request):
    '''
    Listar todos los pagos, o poder hacer un nuevo pago
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