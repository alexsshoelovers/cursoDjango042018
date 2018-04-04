# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db import models
# Create your models here.

class TipoProducto(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50, default='sinnombre')
    tipo_producto =models.ForeignKey(TipoProducto, on_delete=models.PROTECT, related_name='tipo')
    precio = models.FloatField()

    def __str__(self):
        return self.nombre

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


class Elemento_Receta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT,related_name='elementos')
    ingrediente = models.ForeignKey(Ingrediente,on_delete=models.PROTECT,  related_name='elementos')
    cantidad = models.IntegerField()

    def __str__(self):
        return '{} - {} - {}'.format(self.producto.nombre, self.ingrediente.nombre , self.cantidad)

    def __unicode__(self):
        return '{} - {} - {}'.format(self.producto.nombre, self.ingrediente.nombre, self.cantidad)
