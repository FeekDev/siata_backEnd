'''
Conexión a la interface del administrador

Se encarga de leer el módulo que se modeló y así poder
interactuar desde la interface con la base de datos
'''

# Módulos
from django.contrib import admin
from .models import Restaurante


'''
admin.site.register(Restaurante)
----------------
Aquí se crea la acción que permite ahcer
nuevas entradas en la base de datos
'''
@admin.register(Restaurante)
class RestauranteAdmin(admin.ModelAdmin):
    '''
    Filtro de campos
    -------------
    Filtra los campos que se desean mostrar en
    la interface del administrador de base de datos
    '''
    list_display = ['nombreRestaurante', 'identificacionUsuario', 'valorMenu', 'valorPagado']
