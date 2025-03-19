from django.urls import path
from . import views

urlpatterns = [
    path('', views.celular_list, name='celular_list'),
]
