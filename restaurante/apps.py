'''
Aplicacion
---------
Aquí se genera el nombre de pila de 
la aplicación la cual se está desarrollador
'''

# Modulos
from django.apps import AppConfig


class RestauranteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restaurante'
