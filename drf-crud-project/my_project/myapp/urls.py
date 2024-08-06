from django.urls import path
from .views import RegisterView, LoginView
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')

urlpatterns += router.urls