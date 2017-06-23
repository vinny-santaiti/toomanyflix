# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
import urllib

from rating.models import Movie
from rating.serializers import MovieSerializer

import requests
from rest_framework import viewsets
from rest_framework.response import Response

LOG = logging.getLogger(__name__)


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows movies to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def retrieve(self, request, pk=None):
        """
        Get single object
        """
        movie = Movie.objects.get(id=pk)
        self.access_omdb_api(movie=movie)
        serializer = self.get_serializer(movie)
        return Response(serializer.data)

    def access_omdb_api(self, movie):
        """
        Update the movie Metascore and imdbRating from omdb api
        http: // www.omdbapi.com /?t = donnie + darko & y = & plot = short & r = json
        """
        url = 'http://www.omdbapi.com/?i=tt3896198&apikey=f8ef04cb&r=json&plot=short'
        data = {'t': movie.title}
        api_url = '{0}&{1}'.format(url, urllib.urlencode(data))
        response = requests.get(api_url)
        response.raise_for_status()
        json_resp = response.json()
        try:
            movie.metascore = json_resp['Metascore']
            movie.imdbRating = json_resp['imdbRating']
            movie.save()
        except KeyError:
            LOG.error(response.url, exc_info=True)
            pass
