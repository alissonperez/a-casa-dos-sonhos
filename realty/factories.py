import factory
import factory.fuzzy

from . import models


ModelFactory = factory.django.DjangoModelFactory


class ProvinceFactory(ModelFactory):
    class Meta:
        model = models.Province

    name = factory.Faker('company')
    x_u = factory.fuzzy.FuzzyInteger(0, 200)
    y_u = factory.fuzzy.FuzzyInteger(500, 1000)
    x_b = factory.fuzzy.FuzzyInteger(800, 1400)
    y_b = factory.fuzzy.FuzzyInteger(0, 400)



class PropertyFactory(ModelFactory):
    class Meta:
        model = models.Property

    title = factory.Faker('company')
    price = factory.fuzzy.FuzzyDecimal(10000.00, 1200234567.00)
    description = factory.Faker('company')
    x = factory.fuzzy.FuzzyInteger(0, 1400)
    y = factory.fuzzy.FuzzyInteger(0, 1000)
    beds = factory.fuzzy.FuzzyInteger(1, 5)
    baths = factory.fuzzy.FuzzyInteger(1, 4)
    square_meters = factory.fuzzy.FuzzyInteger(20, 240)
