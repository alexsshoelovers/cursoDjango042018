# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from restaurante_app.models import Restaurante
from clientes_app.models import Profile
from catalogo_app.models import TipoProducto,Ingrediente


class Order(models.Model):
    fecha = models.DateField()
    cliente = models.ForeignKey(Profile)
    restaurante = models.ForeignKey(Restaurante)

    def __str__(self):
        return '{} - {}'.format( self.cliente.user.username, self.fecha)

    def __unicode__(self):
        return '{} - {}'.format(self.cliente.user.username, self.fecha)

class Producto_Instance(models.Model):
    tipo_producto = models.ForeignKey(TipoProducto, on_delete=models.PROTECT)
    precio = models.FloatField()
    order= models.ForeignKey(Order, related_name='items')
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{} - {} - {}'.format( self.tipo_producto.nombre,  self.name,  self.precio)

    def __unicode__(self):
        return '{} - {} - {}'.format(self.tipo_producto.nombre, self.name, self.precio)

class Elemento_Receta(models.Model):
    producto = models.ForeignKey(Producto_Instance, related_name='componentes')
    ingrediente = models.ForeignKey(Ingrediente)
    cantidad = models.IntegerField()

    def __str__(self):
        return '{} - {} - {} - {} - {}'.format( self.producto.order.__str__(),self.producto.tipo_producto, self.producto.name , self.ingrediente.nombre, self.cantidad)

    def __unicode__(self):
        return '{} - {} - {} - {} - {}'.format(self.producto.order.__str__(), self.producto.tipo_producto, self.producto.name, self.ingrediente.nombre, self.cantidad)