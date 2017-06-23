# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from rating.models import Movie
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    pass

admin.site.register(Movie, MovieAdmin)
