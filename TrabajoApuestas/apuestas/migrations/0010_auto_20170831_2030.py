# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apuestas', '0009_auto_20170831_0514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apuesta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('partido_id', models.IntegerField()),
                ('credit_amount', models.IntegerField()),
                ('ratio', models.FloatField()),
                ('choice_bet', models.CharField(choices=[('1', 'Gana equipo local'), ('x', 'Empate'), ('2', 'Gana equipo visitante')], max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='equipo',
            name='winrate_init',
            field=models.FloatField(default=0.8446627595214393),
        ),
    ]
