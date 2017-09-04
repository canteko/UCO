# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuestas', '0016_auto_20170902_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='apuesta',
            name='match_finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='partido',
            name='str_bet',
            field=models.CharField(max_length=1, default='0'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='winrate_init',
            field=models.FloatField(default=0.40963472398876577),
        ),
    ]
