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
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from pytz import UTC
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

    '''
    @property
    def validador_Pago(self):
        valor_menu = self.valorMenu
        valor_pagado = self.valorPagado
        if valor_menu == valor_pagado:
            raise serializers.ValidationError('gracias por pagar todo tu arriendo')
            return Response(status=status.HTTP_200_OK)
        else:
            raise serializers.ValidationError('gracias por tu abono, sin embargo recuerda que te hace')

    '''


def datepublished(self):
    return self.pub_date.strftime('%d/%M/%Y')


class Meta:
    ordering = ['nombreRestaurante']
