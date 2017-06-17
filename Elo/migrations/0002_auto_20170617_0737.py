# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='team_id',
            field=models.IntegerField(),
        ),
    ]
