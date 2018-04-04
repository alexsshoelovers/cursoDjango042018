# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-28 03:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ventas_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elemento_receta',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='componentes', to='ventas_app.Producto_Instance'),
        ),
        migrations.AlterField(
            model_name='producto_instance',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='ventas_app.Order'),
        ),
    ]