from django.shortcuts import render
from .models import Celulares

def celular_list(request):
    celulares = Celulares.objects.all()
    return render(request, 'core/celular_list.html', {'celulares': celulares})
