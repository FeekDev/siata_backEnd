'''
Archivo para conectarse al sitio del administrador

Se encarga de leer el módulo que se modeló y así poder
interactuar desde la interface con la base de datos
'''

# Módulos
from django.contrib import admin
from .models import Restaurante

'''
Aquí se crea la acción que permite crear
nuevas entradas en la base de datos
'''
admin.site.register(Restaurante)
