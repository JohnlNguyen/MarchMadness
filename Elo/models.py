from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Rating(models.Model):
    team_name = models.CharField(max_length=100,unique=True)
    team_id = models.IntegerField()
    elo = models.FloatField()

    def __str__(self):
        return "%s, %s, %s" % (str(self.team_id),self.team_name, self.elo)