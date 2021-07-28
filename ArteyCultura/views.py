from email.mime import text
from django import http
from django.http import *
from django.shortcuts import *
from django.core.mail import *
from django.template.loader import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import *

def inicio(request):
    return render(request, "inicio.html")

def correo(request):
    #correo = EmailMessage('Prueba de correo', 'Saludos crack', to = ["gugd2001@hotmail.com"])
    #correo.send()
    plantilla = get_template("correo.html")
    nombre = "Gabo"
    diccionario = {"nombre":nombre}
    body = plantilla.render(diccionario)
    correo = EmailMultiAlternatives(
        "Prueba 2", #asunto
        "Mensaje de prueba", #body
        'gugd2001@hotmail.com', #enviador
        ['gugd2001@gmail.com'], #recibe
        ['luisgqr1975@gmail.com'] #copia oculta
    )
    correo.attach_alternative(body,"text/html")
    correo.send()

    return HttpResponse("Hola")


def log_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            u = request.POST["username"]
            p = request.POST["password"]
            usr = authenticate(username=u, password=p)  
            if usr is not None:
                login(request,usr)
                request.session["session"] = u

    context = {"form":form}
    return render(request, "login.html",context)


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()

    form.fields["username"].help_text = None
    form.fields["password1"].help_text = None
    form.fields["password2"].help_text = None
            

    context = {"form":form}
    return render(request, "register.html",context)


def log_out(request):
    logout(request)
    return HttpResponse("Adios")