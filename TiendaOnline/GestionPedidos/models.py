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

    def __str__(self):
        return " El nombre es {} de la sección {} y su precio {} ".format(self.nombre, self.seccion, self.precio)


class Pedido(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
