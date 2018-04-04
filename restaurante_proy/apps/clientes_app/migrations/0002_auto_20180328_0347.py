# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-28 03:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='tipo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='usuarios', to='clientes_app.TipoUsuario'),
            preserve_default=False,
        ),
    ]