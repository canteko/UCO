# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuestas', '0003_partido_match_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partido',
            name='match_id',
        ),
    ]
