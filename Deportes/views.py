from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import generic

from .forms import *

# Create your views here.


def inicioD(request):
    return HttpResponse("<a href='deporte/add'>Agregar</a>")

def agregarD(request):
    form = DeporteForm()
    if request.method == 'POST':
        form = DeporteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form":form}
    return render (request, "arte.html", context)


class ListaDeportes(generic.ListView):
    model = Deportes
    context_object_name = "ActividadesDeportes"
    template_name = "deportes.html"