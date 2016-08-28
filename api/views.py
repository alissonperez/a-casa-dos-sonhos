from rest_framework import viewsets
from api import serializers
from realty import models


class ProvinceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Province.objects.all()
    serializer_class = serializers.ProvinceSerializer
