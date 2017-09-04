# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuestas', '0015_auto_20170902_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='claimed',
        ),
        migrations.AddField(
            model_name='apuesta',
            name='claimed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='winrate_init',
            field=models.FloatField(default=0.4267109903449404),
        ),
    ]
