# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import TipoProducto
from .models import Producto
from .models import Ingrediente
from .models import Elemento_Receta

# Register your models here.
admin.site.register(TipoProducto)
admin.site.register(Producto)
admin.site.register(Ingrediente)
admin.site.register(Elemento_Receta)