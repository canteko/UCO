# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuestas', '0010_auto_20170831_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='winrate_init',
            field=models.FloatField(default=0.8572905212329479),
        ),
    ]
