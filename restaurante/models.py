'''
Modelación de la base de datos

De acuerdo a los campos que necesitemos en nuestra
base de datos, elegiremos el tipo del campo y las
características de cada una
'''

# Modulos
from django.db import models
from rest_framework import serializers, status
from rest_framework.response import Response
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from datetime import datetime


DATETIME_FORMAT=['%m/%d/%Y']


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
    valorMenu = models.IntegerField(
            null=False,
            validators=[
                MinValueValidator(1),
                MaxValueValidator(1000000)]
    )
    valorPagado = models.IntegerField(
            null=False
    )
    fechaPago = models.DateField(
            auto_now_add=True,
            blank=False
    )

    class Meta:
        ordering = ['nombreRestaurante']


def conversion_Horaria(self):
    '''
    Se realiza con el fin de poder
    tomar los datos necesarios del dia
    que se realizo el pago, sin tener
    que tomar la hora.
    '''
    return self.pub_date.strftime('%d/%M/%Y')
