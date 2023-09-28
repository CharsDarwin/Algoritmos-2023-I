from django.urls import path
from . import views

urlpatterns = [
    # path de la app services

    path("", views.services, name="services"),
]