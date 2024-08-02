from django.urls import path
from . import views
urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('members/create/', views.create_member, name='create_member'),
    path('members/<int:id>/update/', views.update_member, name='update_member'),
    path('members/<int:id>/delete/', views.delete_member, name='delete_member'),
]
