from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError 
from .models import Art,Artista
from .forms import ArtForm
from django.contrib.auth.models import User

# Vista para la página de inicio
def home(request):
    return render(request, 'home.html')

# Vista para la página de ubicación
def ubicacion(request):
    return render(request, 'ubicacion.html')

# Vista para la página de contacto
def contacto(request):
    return render(request, 'contactar.html')

# Vista para la tienda (catalogo de arte)
def tienda(request):
    arts = Art.objects.all()
    return render(request, 'tienda.html', {'arts': arts})

# Vista para el menú (no lo necesitas en tus URLs)
def menu(request):
    return render(request, 'menu.html')

# Vista para el carrito (puedes agregar lógica para manejar el carrito aquí)
def carro(request):
    return render(request, 'carro.html')

# Vista para las redes sociales
def redes(request):
    return render(request, 'redes.html')

# Vista para detalles de una obra de arte específica
def detalles(request):
    return render(request, 'detalles.html')

# Vista para el registro de usuarios
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm()})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm(), "error": "Username already exists."})

        return render(request, 'signup.html', {"form": UserCreationForm(), "error": "Passwords did not match."})

# Vista para el inicio de sesión
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm(), "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('home')

# Vista para agregar una nueva obra de arte
@login_required
def add_art(request):
    if request.method == 'GET':
        form = ArtForm()
        return render(request, 'add_art.html', {'form': form})
    else:
        form = ArtForm(request.POST, request.FILES)
        if form.is_valid():
            art = form.save(commit=False)
            art.save()
            return redirect('art_list')
        else:
            return render(request, 'add_art.html', {'form': form, 'error': 'Error al agregar la obra de arte.'})

# Vista para la lista de todas las obras de arte
def art_list(request):
    arts = Art.objects.all()
    return render(request, 'art_list.html', {'arts': arts})

# Vista para cerrar sesión
@login_required
def signout(request):
    logout(request)
    return redirect('home')  # O redirige a la página de inicio de sesión u otra página de tu elección


# Vista para los detalles de una obra de arte específica
def art_detail(request, art_id):
    art = get_object_or_404(Art, pk=art_id)
    return render(request, 'art_detail.html', {'art': art})