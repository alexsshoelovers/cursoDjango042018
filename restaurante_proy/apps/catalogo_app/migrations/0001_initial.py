# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-28 03:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Elemento_Receta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo_producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tipo', to='catalogo_app.TipoProducto'),
        ),
        migrations.AddField(
            model_name='elemento_receta',
            name='ingrediente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='elementos', to='catalogo_app.Ingrediente'),
        ),
        migrations.AddField(
            model_name='elemento_receta',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='elementos', to='catalogo_app.Producto'),
        ),
    ]
