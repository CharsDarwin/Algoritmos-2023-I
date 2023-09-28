from django.shortcuts import render
from .models import Service

# Create your views here.

def services(request):
    # accediendo al modelo (y guardando todo en la variable services)
    services = Service.objects.all()
    # se envia con un diccionario de contexto
    return render(request, 'services.html',{'services':services})