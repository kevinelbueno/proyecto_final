from django.shortcuts import render

# Create your views here.
  
def home(request): 
    return render(request, "home.html") 
  
def ubicacion(request): 
    return render(request, "ubicacion.html") 
  
def contacto(request): 
    return render(request, "contactar.html")

def tienda(request):
    return render(request, "tienda.html")

def menu(request):
    return render(request, "menu.html")

def carro(request):
    return render(request, "carro.html")

def redes(request):
    return render(request, "redes_sociales.html")