from django.db import models
# libreria para detectar la zona horaria donde esta configurado el proyecto
from django.utils.timezone import now
# importando modelo User que contiene todos los modelos que estan registrados en le panel de administrador
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(verbose_name = 'Contenido')
    published = models.DateTimeField(verbose_name = 'Fecha de publicacion', default = now)
    image = models.ImageField(verbose_name='Imagen', upload_to = 'blog', null=True, blank=True)
    # Utilizando forenkey (llave foranea para relacionar post con User)
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edicion")
    
    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ['-created']

    def __str__(self):
        return self.title
