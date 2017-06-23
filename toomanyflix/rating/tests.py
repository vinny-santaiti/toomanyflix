# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rating.models import Movie

import mock as mock
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestApi(APITestCase):

    def test_get(self):
        url = reverse('movie-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        url = reverse('movie-list')
        data = {'title': 'Wonder Woman'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 1)
        self.assertEqual(Movie.objects.get().title, data['title'])

    @mock.patch('rating.views.requests.get')
    def test_get_one_movie(self, mock_get):
        """test get of single object without connect to api"""
        # mock_get.return_value = mock.MagicMock(**{'status_code': 200, 'return_value': 'ok'})
        rating = {"Metascore": "88", "imdbRating": "8.1"}
        mock_get.return_value = mock.Mock()
        mock_get.return_value.json.return_value = rating
        Movie.objects.create(title='Wonder Woman')
        url = reverse('movie-list')
        response = self.client.get(url + '1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['metascore'], 88)
        self.assertEqual(response.data['imdbRating'], 8.1)

