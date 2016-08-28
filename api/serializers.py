from rest_framework import serializers
from realty import models


class PropertySerializer(serializers.ModelSerializer):
    squareMeters = serializers.IntegerField(source='square_meters',
                                            min_value=20,
                                            max_value=240)
    provinces = serializers.SerializerMethodField()
    beds = serializers.IntegerField(min_value=1, max_value=5)
    baths = serializers.IntegerField(min_value=1, max_value=4)

    class Meta:
        model = models.Property
        fields = ('id', 'title', 'price', 'description', 'x', 'y',
                  'beds', 'baths', 'squareMeters', 'provinces')

    def get_provinces(self, obj):
        return list(self._fetch_provinces(obj.x, obj.y).values_list('name', flat=True))

    def validate(self, data):
        data = self._check_coordinates(data)

        return data

    def _check_coordinates(self, data):
        if self._fetch_provinces(data['x'], data['y']).count() == 0:
            raise serializers.ValidationError('Property doesn\'t to any province.')

        return data

    def _fetch_provinces(self, x, y):
        return models.Province.objects.filter(
            x_u__lte=x, x_b__gte=x,
            y_u__gte=y, y_b__lte=y)
