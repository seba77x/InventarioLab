# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-30 01:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0009_auto_20161129_2113'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lista_atributo',
            unique_together=set([]),
        ),
    ]
