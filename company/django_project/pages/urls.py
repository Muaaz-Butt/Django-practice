from django.urls import path

from .views import *

urlpatterns = [
    path("", home_page_view, name="home"),
    path("about/", AutoPageView.as_view(), name="about"),
]
