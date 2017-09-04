# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuestas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('winrate_init', models.FloatField(default=0.5)),
                ('name', models.CharField(max_length=100)),
                ('won', models.IntegerField(default=0)),
                ('even', models.IntegerField(default=0)),
                ('lost', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('puntos_local', models.IntegerField(default=0)),
                ('puntos_visitante', models.IntegerField(default=0)),
                ('empezado', models.BooleanField(default=False)),
                ('terminado', models.BooleanField(default=False)),
                ('inicio', models.DateTimeField()),
                ('fin', models.DateTimeField()),
                ('local', models.ForeignKey(to='apuestas.Equipo', related_name='partido_local')),
                ('visitante', models.ForeignKey(to='apuestas.Equipo', related_name='partido_visitante')),
            ],
        ),
    ]
