from django.apps import AppConfig


class ServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'services'
    # traduciendo el nombre de la app
    verbose_name = 'Gestor de Servicios'
