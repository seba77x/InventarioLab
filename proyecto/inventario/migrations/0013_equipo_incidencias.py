# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 07:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0012_auto_20161130_0353'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='Incidencias',
            field=models.ManyToManyField(through='inventario.Lista_Incidencia', to='inventario.Incidencia'),
        ),
    ]
