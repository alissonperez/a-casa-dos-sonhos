from django.test import TestCase

from api import serializers
from realty import factories


class PropertyTestCase(TestCase):

    def test_serializer_has_fields(self):
        prov = factories.ProvinceFactory()
        prop = factories.PropertyFactory(x=prov.x_u+10,
                                         y=prov.y_u-10)
        serializer = serializers.PropertySerializer(prop)

        expected_fields = {
            'id',
            'title',
            'price',
            'description',
            'x',
            'y',
            'beds',
            'baths',
            'provinces',
            'squareMeters',
        }

        fields = set(dict(serializer.data).keys())
        self.assertEqual(fields, expected_fields)

    def test_serializer_has_correct_price(self):
        prop = factories.PropertyFactory(price=12000.00)
        serializer = serializers.PropertySerializer(prop)

        self.assertEqual(serializer.data['price'], 12000.00)

    def test_serializer_has_correct_province(self):
        prov = factories.ProvinceFactory()
        prop = factories.PropertyFactory(x=prov.x_u+10,
                                         y=prov.y_u-10)

        serializer = serializers.PropertySerializer(prop)

        self.assertEqual(serializer.data['provinces'], [prov.name])

    def test_serializer_must_not_belongs_to_other_province(self):
        prov = factories.ProvinceFactory(x_u=0, y_u=10,
                                         x_b=10, y_b=0)

        prop = factories.PropertyFactory(x=100)

        serializer = serializers.PropertySerializer(prop)

        self.assertEqual(serializer.data['provinces'], [])

    def test_serializer_must_create_model_with_correct_values(self):
        prov = factories.ProvinceFactory(x_u=0, y_u=10,
                                         x_b=10, y_b=0)

        values = self._valid_property_dict

        serializer = serializers.PropertySerializer(data=values)
        self.assertTrue(serializer.is_valid())

        model = serializer.save()

        self.assertEqual(model.title, values['title'])
        self.assertEqual(model.price, values['price'])
        self.assertEqual(model.description, values['description'])
        self.assertEqual(model.x, values['x'])
        self.assertEqual(model.y, values['y'])
        self.assertEqual(model.beds, values['beds'])
        self.assertEqual(model.baths, values['baths'])
        self.assertEqual(model.square_meters, values['squareMeters'])

    def test_serializer_creation_validate_if_prop_belongs_to_province(self):
        prov = factories.ProvinceFactory(x_u=0, y_u=10,
                                         x_b=10, y_b=0)

        values = self._valid_property_dict

        # changing x to outside of our test province
        values['x'] = 20

        serializer = serializers.PropertySerializer(data=values)
        self.assertFalse(serializer.is_valid())

    def test_serializer_must_validate_beds(self):
        prov = factories.ProvinceFactory(x_u=0, y_u=10,
                                         x_b=10, y_b=0)

        values = self._valid_property_dict

        # Min value is 1
        values['beds'] = 0

        serializer = serializers.PropertySerializer(data=values)
        self.assertFalse(serializer.is_valid())

        # Max value is 5
        values['beds'] = 6

        serializer = serializers.PropertySerializer(data=values)
        self.assertFalse(serializer.is_valid())

        values['beds'] = 5

        serializer = serializers.PropertySerializer(data=values)
        self.assertTrue(serializer.is_valid())

    def test_serializer_must_validate_baths(self):
        prov = factories.ProvinceFactory(x_u=0, y_u=10,
                                         x_b=10, y_b=0)

        values = self._valid_property_dict

        # Min value is 1
        values['baths'] = 0

        serializer = serializers.PropertySerializer(data=values)
        self.assertFalse(serializer.is_valid())

        # Max value is 4
        values['baths'] = 5

        serializer = serializers.PropertySerializer(data=values)
        self.assertFalse(serializer.is_valid())

        values['baths'] = 4

        serializer = serializers.PropertySerializer(data=values)
        self.assertTrue(serializer.is_valid())

    def test_serializer_must_validate_square_meters(self):
        prov = factories.ProvinceFactory(x_u=0, y_u=10,
                                         x_b=10, y_b=0)

        values = self._valid_property_dict

        # Min value is 20
        values['squareMeters'] = 19

        serializer = serializers.PropertySerializer(data=values)
        self.assertFalse(serializer.is_valid())

        # Max value is 4
        values['squareMeters'] = 300

        serializer = serializers.PropertySerializer(data=values)
        self.assertFalse(serializer.is_valid())

        values['squareMeters'] = 240

        serializer = serializers.PropertySerializer(data=values)
        self.assertTrue(serializer.is_valid())

    @property
    def _valid_property_dict(self):
        return {
            'title': 'Test property',
            'price': 450000.00,
            'description': 'Property description',
            'x': 5,
            'y': 5,
            'beds': 3,
            'baths': 3,
            'squareMeters': 100,
        }


class ProvinceTestCase(TestCase):

    def test_serializer_has_fields(self):
        prov = factories.ProvinceFactory()
        serializer = serializers.ProvinceSerializer(prov)

        expected_fields = {
            'id',
            'name',
            'xUp',
            'yUp',
            'xBottom',
            'yBottom',
        }

        fields = set(dict(serializer.data).keys())
        self.assertEqual(fields, expected_fields)
