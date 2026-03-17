from django.shortcuts import render
from contenido import models
from django.core.paginator import Paginator
from django.core.exceptions import ValidationError

# Create your views here.

def formulario(request):
    todas_las_personas = models.Persona.objects.all()
    paginator = Paginator(todas_las_personas,2)
    numero_pagina = request.GET.get('page',1)
    numero_pagina = int(numero_pagina)

    if numero_pagina < 1:
        numero_pagina = 1
    elif numero_pagina > paginator.num_pages:
        numero_pagina = paginator.num_pages
        
    pagina = paginator.page(numero_pagina)

    return render(
        request,
        'templates/formulario.html',
        {"personas":pagina.object_list,"pagina":numero_pagina}
    )