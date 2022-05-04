from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from drf_dynamic_fields import DynamicFieldsMixin
from . import models

from diana.abstract.models import get_fields

class ObjectSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Object
        fields = get_fields(models.Object)
        depth = 1

class ParishSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Parish
        fields = '__all__'
        depth = 1

class PlaceSerializer(DynamicFieldsMixin, GeoFeatureModelSerializer):
    class Meta:
        model = models.Place
        fields = get_fields(models.Place)
        geo_field = 'geom'

class MotiveSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Motive
        fields = '__all__'
        depth = 1

class ImageSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = '__all__'