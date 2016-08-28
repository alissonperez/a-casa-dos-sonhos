from django.urls import reverse
from django.test import TestCase, Client

from realty import factories
from api import serializers


class ProvincesTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_listing(self):
        url = reverse('province-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_listing_must_have_province(self):
        prov = factories.ProvinceFactory()
        url = reverse('province-list')

        response = self.client.get(url)

        serializer = serializers.ProvinceSerializer(prov)

        self.assertIn(serializer.data, response.data)
