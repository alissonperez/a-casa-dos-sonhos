from django.test import TestCase
from django.db.utils import IntegrityError

from realty import models


class ProviceTestCase(TestCase):

    def test_item_creation(self):
        provice = models.Province.objects.create(
            name='Gode',
            # Boundaries
            x_u=0, y_u=1000,
            x_b=600, y_b=5000,
        )

    def test_duplicated_name_must_raise_exception(self):
        params = dict(
            name='Gode',
            # Boundaries
            x_u=0, y_u=1000,
            x_b=600, y_b=5000,
        )

        provice = models.Province.objects.create(**params)

        self.assertRaises(IntegrityError, models.Province.objects.create, **params)


class PropertyTestCase(TestCase):

    def test_item_creation(self):
        prop = models.Property.objects.create(
            title='Test property',
            price=1250000,
            description='Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            x=870,
            y=867,
            beds=5,
            baths=4,
            square_meters=134
        )
