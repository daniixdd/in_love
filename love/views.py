from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
# Vista para el registro de un nuevo usuario
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import Articulos
from .models import Articulos, ItemCarrito
from django.shortcuts import render, redirect
from .models import Reseña2
from .forms import ReseñaForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile  # Asegúrate de importar tu modelo Profile
from .forms import UserProfileForm  

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu perfil ha sido actualizado correctamente.')
            return redirect('profile')  # Redirige de nuevo a la página de perfil
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'profile.html', {'form': form})


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)  # Crea un perfil automáticamente cuando un nuevo usuario se registre

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()  # Guarda el perfil cada vez que se guarda el usuario

@login_required
def editprofile(request):
    # Lógica para editar el perfil
    return render(request, 'tienda/editprofile.html')

def reseña2(request):
    if request.method == 'POST':
        form = ReseñaForm(request.POST)
        if form.is_valid():
            reseña = form.save(commit=False)  # No guardamos aún
            reseña.usuario = request.user  # Asignamos el usuario que está logueado
            reseña.nombre = request.user.username  # Usamos el nombre del usuario automáticamente
            reseña.save()  # Guardamos la reseña
            return redirect('reseña2')  # Redirigimos para que no se repita el envío
    else:
        form = ReseñaForm()

    # Obtenemos todas las reseñas para mostrarlas
    todas_reseñas = Reseña2.objects.all().order_by('-fecha')

    return render(request, 'tienda/reseña2.html', {
        'form': form,
        'reseñas': todas_reseñas,
    })

def profile(request):
    # Lógica para la vista 'profile'
    return render(request, 'tienda/profile.html')  # Asegúrate de tener la plantilla 'profile.html'

def home(request):
    productos = Articulos.objects.all()
    return render(request, 'tienda/home.html', {'productos': productos})

def index(request):
    productos = Articulos.objects.all()  # Puedes mostrar los productos en la página de inicio
    return render(request, 'tienda/index.html', {'productos': productos})

def carrito(request):
    productos = Articulos.objects.all()  # Puedes mostrar los productos en la página de inicio
    return render(request, 'tienda/carrito.html', {'productos': productos})

def articulos(request):
    productos_disponibles = Articulos.objects.filter(stock__gt=0)  # Solo artículos con stock disponible
    if not productos_disponibles.exists():
        messages.info(request, "No hay artículos disponibles en este momento. ¡Vuelve pronto para ver nuestras novedades!")
    return render(request, 'tienda/articulos.html', {'productos': productos_disponibles})



def articulos2(request):
    productos2_disponibles = Articulos.objects.filter(stock__gt=0)  # Solo artículos con stock disponible
    return render(request, 'tienda/articulos2.html', {'productos2': productos2_disponibles})



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


def user_register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']  # Obtener el correo electrónico

        # Validar que las contraseñas coincidan
        if password != password2:
            messages.error(request, "Las contraseñas no coinciden.")
            return redirect('register')

        # Validar que el usuario no exista
        if User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe.")
            return redirect('register')

        # Validar que el correo electrónico no esté en uso
        if User.objects.filter(email=email).exists():
            messages.error(request, "Este correo electrónico ya está en uso.")
            return redirect('register')

        # Crear el usuario con correo electrónico
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        # Iniciar sesión automáticamente al registrarse
        login(request, user)
        messages.success(request, "Te has registrado y autenticado con éxito.")
        return redirect('index')  # Redirige a la página principal

    return render(request, 'tienda/register.html')


