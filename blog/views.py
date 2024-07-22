from django.shortcuts import render
from .models import Carne, Bebida


def post_list(request):
    # Lógica para la lista de publicaciones
    return render(request, 'blog/post_list.html')

def carne_list(request):
    carnes = Carne.objects.all()
    return render(request, 'blog/carne_list.html', {'carnes': carnes})

def bebida_list(request):
    bebidas = Bebida.objects.all()
    return render(request, 'blog/bebida_list.html', {'bebidas': bebidas})



