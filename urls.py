from django.urls import path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

from . import views

import diana.utils as utils

router = routers.DefaultRouter()

# Manual viewsets
router.register(r'api/object', views.ObjectViewSet, basename='object')
router.register(r'api/place', views.PlaceViewSet, basename='place')

urlpatterns = [
    path('', include(router.urls)),
    path('api/schema/', get_schema_view(
        title="Iconographia",
        description="Schema for the Iconographia API at the Centre for Digital Humanities",
        version="1.0.0",
        urlconf="diana.urls"
    ), name='openapi-schema'),
    path('documentation/', TemplateView.as_view(
        template_name='redoc-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='redoc-ui'),

    # Automatically generated views
    *utils.get_model_urls('iconographia', 'api', exclude=['object', 'place', 'collabels']),
]