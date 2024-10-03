from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('helloworld/', views.helloworld, name='helloworld'),
  path('members/', views.members, name='members'),
  path('members/details/<int:id>', views.details, name='details')
]
