# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuestas', '0014_auto_20170902_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='claimed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='winrate_init',
            field=models.FloatField(default=0.808429574320161),
        ),
    ]
