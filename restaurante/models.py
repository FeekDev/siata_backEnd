'''
Modelación de la base de datos

De acuerdo a los campos que necesitemos en nuestra
base de datos, elegiremos el tipo del campo y las
Características de cada una
'''

# Modulos
from django.db import models
from rest_framework import serializers, status
from rest_framework.response import Response
from django.core.validators import RegexValidator
from datetime import datetime

'''
def validator_nombreRestaurante(value):
    if "12345678910" in value:
        raise serializers.ValidationError('Formato de nombre incorrecto')
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return value
'''

class Restaurante(models.Model):
    '''
    Se crea la clase Restaurante

    Descripción:
    - Esta clase es heredada de models.
    - cada atributo de la clase es un campo de la base de datos.
    '''
    nombreRestaurante = models.CharField(
                    max_length=30,
                    validators=[
                        RegexValidator(
                            regex='^[a-zA-Z ]*$',
                            message='Formato de nombre incorrecto',
                        ),
                    ]
    )
    identificacionUsuario = models.BigIntegerField(null=False)
    menú = models.CharField(
        max_length=100,
        null=False,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z0-9, ]*$',
                message='Debe ser alfanúmerico',
            ),
        ]
    )
    valorMenu = models.BigIntegerField(null=False)
    valorPagado = models.BigIntegerField(null=False)
    fechaPago = models.DateField(blank=False, default=datetime.now().date())


class Meta:
    ordering = ['nombreRestaurante']
