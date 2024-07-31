from django.urls import path
from .views import *

urlpatterns = [
    path("about/", about_page_view),
    path("", home_page_view),
]
