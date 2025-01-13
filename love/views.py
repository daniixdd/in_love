from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Producto

# Vista para listar los productos
def home(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/home.html', {'productos': productos})

def index(request):
    productos = Producto.objects.all()  # Puedes mostrar los productos en la página de inicio
    return render(request, 'tienda/index.html', {'productos': productos})

def articulos(request):
    productos = Producto.objects.all()  # Puedes mostrar los productos en la página de inicio
    return render(request, 'tienda/articulos.html', {'productos': productos})

# Vista para el login
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirige a la página principal o a la que prefieras
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
    return render(request, 'tienda/login.html')

# Vista para el logout
def user_logout(request):
    logout(request)
    return redirect('login')  # Redirige a la página de inicio de sesión después de cerrar sesión


def reseñas(request):
    # Lógica de la vista
    context = {
        "reseñas": ["Reseña 1", "Reseña 2", "Reseña 3"],
    }
    return render(request, "tienda/reseñas.html", context)


# Vista para el registro de un nuevo usuario
def user_register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Validar que las contraseñas coincidan
        if password != password2:
            messages.error(request, "Las contraseñas no coinciden.")
            return redirect('register')

        # Validar que el usuario no exista
        if User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe.")
            return redirect('register')

        # Crear el usuario
        user = User.objects.create_user(username=username, password=password)
        user.save()

        # Iniciar sesión automáticamente al registrarse
        login(request, user)
        messages.success(request, "Te has registrado y autenticado con éxito.")
        return redirect('index')  # Redirige a la página principal

    return render(request, 'tienda/register.html')

