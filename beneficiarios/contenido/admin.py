from django.contrib import admin
from unfold.admin import ModelAdmin as UnfoldModelAdmin
from contenido import models

# Register your models here.

@admin.register(models.Persona)
class PersonaAdmin(UnfoldModelAdmin):
    list_display = ("cedula", )