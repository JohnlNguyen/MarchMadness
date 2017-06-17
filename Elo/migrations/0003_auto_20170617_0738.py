# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from Elo.predictor import mean_elo_dict

def combine_names(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Rating = apps.get_model('Elo', 'Rating')
    for key,value in mean_elo_dict.items():
        Rating.objects.create(team_name=value[1],team_id=key,elo=value[0])

class Migration(migrations.Migration):

    dependencies = [
        ('Elo', '0002_auto_20170617_0737'),
    ]

    operations = [
        migrations.RunPython(combine_names),
    ]
