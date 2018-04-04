# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from  .models import Order,Producto_Instance, Elemento_Receta
# Register your models here.
admin.site.register(Producto_Instance)
admin.site.register(Order)
admin.site.register(Elemento_Receta)