from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ruta para la página principal
    path('index/', views.index, name='index'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('reseñas/', views.reseñas, name='reseñas'),
    path('articulos/', views.articulos, name='articulos'),
]
# Agrega las rutas estáticas al final, si está en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
