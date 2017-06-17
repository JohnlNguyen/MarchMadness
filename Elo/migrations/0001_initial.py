# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('team_name', models.CharField(unique=True, max_length=100)),
                ('team_id', models.IntegerField(max_length=100)),
                ('elo', models.FloatField()),
            ],
        ),
    ]
