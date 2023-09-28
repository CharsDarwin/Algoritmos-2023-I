# urls propios del app core 

from django.urls import path
from . import views

urlpatterns = [
    # path del core
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("sample/", views.sample, name="sample"),
    path("visit/", views.visit, name="visit"),
]