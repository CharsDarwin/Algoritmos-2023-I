from django.shortcuts import render
# cargando el modelo Post para acceder a los posts
from .models import Post

# Create your views here.
def blog(request):
    # pasando los post del modulo post a la variable posts
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts':posts})