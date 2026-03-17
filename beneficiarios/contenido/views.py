from django.shortcuts import render
from contenido import models
from django.core.paginator import Paginator
from django.core.exceptions import ValidationError

# Create your views here.

def formulario(request):
    todas_las_personas = models.Persona.objects.all()
    paginator = Paginator(todas_las_personas,2) # Paso todos los objetos a Paginator y 
                                                # el numero que quiero mostrar por pagina
    numero_pagina = request.GET.get('page',1) # El metodo GET es un diccionario que contiene las llaves 
                                            # de los parametros de consulta. Busco page en el diccionario y 
                                            # si no lo encuentro, que por defecto ponga 1
    numero_pagina = int(numero_pagina) # Conviero el numero de page a entero

    if numero_pagina < 1: # Si el usuario digital en la url un numero menor a 1, entonces que por defecto tome 1
        numero_pagina = 1
    elif numero_pagina > paginator.num_pages: # Si el usuario digital en la url un numero mayor 
                                            # al numero de paginas que contiene paginator, entonces que ponga
                                            # el numero maximo disponible que existe en paginator
        numero_pagina = paginator.num_pages

    pagina = paginator.page(numero_pagina) # Paginator toma ahora el numero condicionado de la pagina

    return render(
        request,
        'formulario.html',
        {"personas":pagina.object_list, # object_list son los objetos que se encuentran en la pagina
         "pagina":pagina} # Supongamos que el numero de pagina es dos, como es dos, 
                        # puedo saber si existen objetos en otras paginas con metodos como: has_next, has_previous
    )