from django.db import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Si deseas personalizar la visualización de User
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    search_fields = ('username', 'email')

# Re-registrar el modelo User con el UserAdmin personalizado
admin.site.unregister(User)  # Primero desregistramos el modelo User
admin.site.register(User, CustomUserAdmin)  # Luego lo volvemos a registrar con la personalización

class Articulos(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='articulos/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class ItemCarrito(models.Model):
    articulo = models.ForeignKey(Articulos, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.articulo.nombre}"

class Articulos2(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre


class Reseña2(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    nombre = models.CharField(max_length=100)
    reseña = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reseña de {self.nombre}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relacionado con el usuario
    phone_number = models.CharField(max_length=15, null=True, blank=True)  # Número de teléfono
    # Otros campos que quieras agregar al perfil

    def __str__(self):
        return self.user.username