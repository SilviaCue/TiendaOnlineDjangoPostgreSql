from django.db import models

# Create your models here.


class Clientes(models.Model):
    nombre = models.CharField(max_length=80)
    direccion = models.CharField(max_length=180)
    email = models.EmailField()
    tfno = models.CharField(max_length=9)


class Articulos(models.Model):
    nombre = models.CharField(max_length=80)
    seccion = models.CharField(max_length=80)
    precio = models.IntegerField()


class Pedido(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
