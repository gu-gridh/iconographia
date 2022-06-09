from rest_framework import viewsets
from rest_framework.schemas.openapi import AutoSchema
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_gis.filters import InBBoxFilter
from rest_framework_gis.pagination import GeoJsonPagination
from . import models, serializers

from diana.abstract.views import CountModelMixin, GenericPagination
from diana.abstract.models import get_fields

class ObjectViewSet(viewsets.ReadOnlyModelViewSet, CountModelMixin):
    queryset = models.Object.objects.all()
    serializer_class = serializers.ObjectSerializer
    pagination_class = GenericPagination

    # GIS filters
    bbox_filter_field = 'place__geom'
    filter_backends = [InBBoxFilter, DjangoFilterBackend]
    filterset_fields = get_fields(models.Object) + [f"place__{field}" for field in get_fields(models.Place, exclude="geom")]

    schema = AutoSchema()

class PlaceViewSet(viewsets.ReadOnlyModelViewSet, CountModelMixin):

    queryset = models.Place.objects.all()
    serializer_class = serializers.PlaceSerializer
    filter_backends = [InBBoxFilter, DjangoFilterBackend]
    schema = AutoSchema()
    
    # GIS filters
    bbox_filter_field = 'geom'
    # bbox_filter_include_overlapping = True # Optional

    # Generic filters
    filterset_fields = models.get_fields(models.Place, exclude=['id', 'geom'])

    # Specialized pagination
    pagination_class = GeoJsonPagination
