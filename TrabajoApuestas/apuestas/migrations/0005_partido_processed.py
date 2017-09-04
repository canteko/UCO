# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuestas', '0004_remove_partido_match_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='partido',
            name='processed',
            field=models.BooleanField(default=False),
        ),
    ]
