# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuestas', '0013_auto_20170902_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bets',
            field=models.ManyToManyField(to='apuestas.Apuesta'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='winrate_init',
            field=models.FloatField(default=0.45988074173059157),
        ),
    ]
