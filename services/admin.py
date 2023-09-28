from django.contrib import admin
# importando el modelo para poder tenerlo en el admin de django
from .models import Service


# Register your models here.

# Creando una condiguracion basica para le administrador
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# registrando el servicio y su configuracion
admin.site.register(Service,ServiceAdmin)