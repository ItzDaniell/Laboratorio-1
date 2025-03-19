from django.shortcuts import render

from .models import Item # Importamos el modelo Item 

def item_list(request):
    items = Item.objects.all()
    return render(request, 'core/item_list.html', {'items': items}) # Retorna el 

