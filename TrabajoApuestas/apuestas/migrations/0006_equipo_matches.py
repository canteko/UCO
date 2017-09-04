# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuestas', '0005_partido_processed'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='matches',
            field=models.IntegerField(default=5),
        ),
    ]
