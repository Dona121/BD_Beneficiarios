from django.shortcuts import render
from contenido import models

# Create your views here.

def formulario(request):
    personas = models.Persona.objects.all()
    return render(
        request,
        'templates/formulario.html',
        {"personas":personas}
    )