from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('main_app/create', views.ItemCreate.as_view(), name='add'),
  path('main_app/delete/', views.ItemDelete.as_view(), name='delete'),
]