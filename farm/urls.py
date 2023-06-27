from django.urls import path, include
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("farms/all", views.all_farms, name="all_farms"),
    path("farm/create", views.create_farm, name="create_farm"),
    path("farm/<int:farm_id>/", views.farm_detail, name="farm_detail"),
    path("farm/<int:farm_id>/create_field", views.create_farm_field, name="create_farm_field")
]
