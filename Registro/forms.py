from django import forms

from .models import *

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ["nombre", "apellidos", "correo","sexo"]