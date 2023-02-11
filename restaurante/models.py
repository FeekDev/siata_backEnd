'''
Modelación de la base de datos

De acuerdo a los campos que necesitemos en nuestra
base de datos, elegiremos el tipo del campo y las
Características de cada una
'''

# Modulos
from django.db import models



class Restaurante(models.Model):
    '''
    Se crea la clase Restaurante

    Descripción:
    - Esta clase es heredada de models.
    - cada atributo de la clase es un campo de la base de datos.
    '''
    nombreRestaurante = models.CharField(max_length=25, null=False)
    identificacionUsuario = models.BigIntegerField(null=False)
    menu = models.CharField(max_length=100, null=False)
    valorMenu = models.BigIntegerField(null=False)
    fechaPago = models.DateTimeField(auto_now=True)
    valorPagado = models.BigIntegerField(null=False)

class Meta:
    ordering = ['nombreRestaurante']