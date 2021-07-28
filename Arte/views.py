from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic

from Arte.forms import *

# Create your views here.

def inicioA(request):
    return render(request, "arte.html")

def agregar(request):
    form = ArteForm()
    if request.method == 'POST':
        form = ArteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form":form}
    return render (request, "arte.html", context)


class ListaActividades(generic.ListView):
    model = Arte
    context_object_name = "ActividadesArte"
    template_name = "arte.html"