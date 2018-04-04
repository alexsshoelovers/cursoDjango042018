# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Create your models here.
from django.db import models



class Restaurante(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    open_time= models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Address(models.Model):
    """
    La documentación va aquí
    """
    restaurante = models.ForeignKey(Restaurante)
    street = models.CharField(max_length=50)
    int_number = models.CharField(max_length=50)
    neighborhood = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=30)

