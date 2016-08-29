from rest_framework import viewsets
from api import serializers
from realty import models


class ProvinceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Province.objects.all()
    serializer_class = serializers.ProvinceSerializer
    pagination_class = None


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = models.Property.objects.all()
    serializer_class = serializers.PropertySerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        rect_search = {'ax', 'ay', 'bx', 'by'}
        if rect_search.issubset(self.request.query_params):
            p = self.request.query_params
            queryset = queryset.filter(
                x__gte=p['ax'], x__lte=p['bx'],
                y__gte=p['by'], y__lte=p['ay'])

        return queryset
