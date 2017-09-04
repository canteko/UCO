# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuestas', '0002_equipo_partido'),
    ]

    operations = [
        migrations.AddField(
            model_name='partido',
            name='match_id',
            field=models.IntegerField(default=-1),
        ),
    ]
