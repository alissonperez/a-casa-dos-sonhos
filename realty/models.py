from django.db import models


class Province(models.Model):
    name = models.CharField(max_length=30, unique=True)

    # Upper left
    x_u = models.IntegerField()
    y_u = models.IntegerField()

    # Bottom right
    x_b = models.IntegerField()
    y_b = models.IntegerField()


class Property(models.Model):
    title = models.CharField(max_length=125)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=255)
    x = models.IntegerField()
    y = models.IntegerField()
    beds = models.IntegerField()
    baths = models.IntegerField()
    square_meters = models.IntegerField()
