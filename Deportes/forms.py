from django import forms
from django.forms import fields

from .models import *

class DeporteForm(forms.ModelForm):
    class Meta:
        model = Deportes
        fields = ["nombre", "descripcion"]