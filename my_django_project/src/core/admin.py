from django.contrib import admin
from .models import Item

# Registrar el modelo Item en el panel de administración
admin.site.register(Item)
