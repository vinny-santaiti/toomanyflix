# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=50)
    rating = models.FloatField(default=0)
    metascore = models.IntegerField(default=0)
    imdbRating = models.FloatField(default=0)

    # http://www.omdbapi.com/?t=Donnie+Darko&i=tt3896198&apikey=f8ef04cb

