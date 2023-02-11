from django.db import models

# model

class Restaurante(models.Model):
    nombreRestaurante = models.CharField(max_length=25, null=False)
    identificacionUsuario = models.BigIntegerField(null=False)
    menu = models.CharField(max_length=100)
    valorMenu = models.BigIntegerField(null=False)
    fechaPago = models.DateTimeField()
    valorPagado = models.BigIntegerField(null=False)

class Meta:
    ordering = ['nombreRestaurante']