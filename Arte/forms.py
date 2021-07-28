from django import forms
from django.forms import fields

from .models import *

class ArteForm(forms.ModelForm):
    class Meta:
        model = Arte
        fields = ["nombre", "descripcion"]