# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class TipoUsuario(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    tipo= models.ForeignKey(TipoUsuario, on_delete=models.PROTECT, related_name='usuarios')

    def __str__(self):
        return str(self.user.username)


class Direccion(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
