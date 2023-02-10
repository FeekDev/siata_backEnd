from django.db import models
from django.core.validators import RegexValidator

# model

class Person(models.Model):
    nombreRestaurante = models.CharField(max_length=25, null=False)
    identificacionUsuario = models.BigIntegerField(max_length=10, null=False)
    menú = RegexValidator(r'^[0-100a-zA-Z]*$', null=False)
    valorMenu = models.BigIntegerField(max_length=7, null=False)
    fechaPago = models.DateField(auto_now=False, auto_now_add=True)
    valorPagado = models.BigIntegerField(max_length=7, null=False)