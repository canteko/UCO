# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuestas', '0011_auto_20170831_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='partido',
            name='ratio_even',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='partido',
            name='ratio_local',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='partido',
            name='ratio_visitante',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='winrate_init',
            field=models.FloatField(default=0.42449490071891083),
        ),
    ]
