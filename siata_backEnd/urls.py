'''
Rutas
------
Desde aquí se crean las rutas o endpoints
de acuerdo a las características que deba
poseer o el distintivo con las demás
'''

# Modulos
from django.contrib import admin
from django.urls import path, include
from restaurante import views


# Rutas
urlpatterns = [
    path('admin/', admin.site.urls), # Interface para administrar la base de datos
    path('', views.index, name='index'), # pagina de inicio
    path('api/pagos', views.api_pagos) # Ruta definida para la API
]
