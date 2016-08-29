from django.urls import reverse
from django.test import TestCase, Client

from realty import factories, models
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


class PropertiesTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_listing(self):
        prop = factories.PropertyFactory()
        url = reverse('property-list')

        response = self.client.get(url)

        self.assertEqual(response.data['count'], 1)

        serializer = serializers.PropertySerializer(prop)
        self.assertIn(serializer.data, response.data['results'])

    def test_listing_with_search(self):
        prop_north = factories.PropertyFactory(x=1, y=10)
        prop_soulth = factories.PropertyFactory(x=1, y=1)

        url = reverse('property-list') + '?ax=0&ay=5&bx=2&by=0'

        response = self.client.get(url)

        self.assertEqual(response.data['count'], 1)

        serializer = serializers.PropertySerializer(prop_soulth)
        self.assertIn(serializer.data, response.data['results'])

    def test_retrieve_must_return_correct_property(self):
        prop = factories.PropertyFactory(x=1, y=10)
        url = reverse('property-detail', args=[prop.id])

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        serializer = serializers.PropertySerializer(prop)
        self.assertEqual(response.data, serializer.data)

    def test_properties_creation(self):
        prov = factories.ProvinceFactory(
            x_u=0, y_u=500,
            x_b=300, y_b=0)

        data = {
            'x': 222,
            'y': 444,
            'title': 'Imóvel código 1, com 5 quartos e 4 banheiros',
            'price': 1250000,
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'beds': 4,
            'baths': 3,
            'squareMeters': 210
        }

        self.assertEqual(models.Property.objects.all().count(), 0)

        url = reverse('property-list')
        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, 201)

        self.assertEqual(models.Property.objects.all().count(), 1)

    def test_property_delete_must_not_be_enabled(self):
        prop = factories.PropertyFactory(x=1, y=10)
        url = reverse('property-detail', args=[prop.id])

        response = self.client.delete(url)
        self.assertEqual(response.status_code, 405)
