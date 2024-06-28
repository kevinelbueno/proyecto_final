from django.shortcuts import render
from .models import Artista, Arte
# Create your views here.
  
def home(request): 
    return render(request, "home.html") 
  
def ubicacion(request): 
    return render(request, "ubicacion.html") 
  
def contacto(request): 
    return render(request, "contactar.html")

def tienda(request):
    arte = Arte.objects.all()
    context={"Arte":arte}
    return render(request, "tienda.html", context)

def menu(request):
    return render(request, "menu.html")

def carro(request):
    return render(request, "carro.html")

def redes(request):
    return render(request, "redes_sociales.html")

def detalles(request, nombre_Arte):
    artes = Arte.objects.get(nom = nombre_Arte)
    context= artes.item_set.get(id)
    return render(request, "detalles2.html", context)
def agregar(request):
    return render(request, "agregar.html")

def incio_sesion(request):
    return render(request, "inicio_sesion")