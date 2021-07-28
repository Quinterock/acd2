from django.shortcuts import redirect, render
from django.core.mail import *
from django.template.loader import *
from django.views import generic

from .forms import *

# Create your views here.
def registro(request):
    form = RegistroForm()
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            nombre = request.POST['nombre']
            correo = request.POST['correo']
            plantilla = get_template("correo.html")
            context = {"nombre" : nombre}
            body = plantilla.render(context)
            mail = EmailMultiAlternatives(
                "Prueba 2", #asunto
                "Mensaje de prueba registro", #body
                'gugd2001@gmail.com', #enviador
                [correo], #recibe
                #['luisgqr1975@gmail.com'], #recibe
                ['jrendon@edu.uag.mx'] #copia oculta
            )
            mail.attach_alternative(body,"text/html")
            mail.send()
           
            return redirect("/")
    context = {"form" : form}
    return render(request, 'registro.html', context)
    
class Registrados(generic.ListView):
    model = Persona
    context_object_name = "Registrados"
    template_name = "regis.html"