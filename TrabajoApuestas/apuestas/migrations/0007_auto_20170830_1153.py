# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuestas', '0006_equipo_matches'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='even',
        ),
        migrations.RemoveField(
            model_name='equipo',
            name='lost',
        ),
        migrations.RemoveField(
            model_name='equipo',
            name='won',
        ),
    ]
