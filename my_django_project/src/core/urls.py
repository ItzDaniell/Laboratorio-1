from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),  # Ruta para la vista que muestra la lista de Items
]
