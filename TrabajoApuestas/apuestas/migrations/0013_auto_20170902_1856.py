# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuestas', '0012_auto_20170901_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apuesta',
            name='choice_bet',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='winrate_init',
            field=models.FloatField(default=0.041101652426547175),
        ),
    ]
