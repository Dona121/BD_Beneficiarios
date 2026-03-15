from django.urls import path
from contenido import views

urlpatterns = [
    path('formulario/',views.formulario,name="formulario"),
]