# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-28 18:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atributo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreAtributo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Incidencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsable', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Lista_Atributo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=30)),
                ('idAtributo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Atributo')),
                ('idEquipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Lista_Incidencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idEquipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Equipo')),
                ('idIncidencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Incidencia')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTipo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreSala', models.CharField(max_length=10)),
                ('tipoUbicacion', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='equipo',
            name='estadoEquipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Estado'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='tipoEquipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Tipo_Equipo'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='ubicacionEquipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Ubicacion'),
        ),
        migrations.AlterUniqueTogether(
            name='lista_incidencia',
            unique_together=set([('idEquipo', 'idIncidencia')]),
        ),
        migrations.AlterUniqueTogether(
            name='lista_atributo',
            unique_together=set([('idEquipo', 'idAtributo')]),
        ),
    ]
