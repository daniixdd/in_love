from django import forms
from .models import Reseña2
from django.contrib.auth.models import User


class ReseñaForm(forms.ModelForm):
    class Meta:
        model = Reseña2
        fields = ['reseña']  # Solo el campo reseña, ya que el nombre se asigna automáticamente en la vista
        widgets = {
            'reseña': forms.Textarea(attrs={'placeholder': 'Escribe tu opinión aquí...', 'rows': 4}),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']