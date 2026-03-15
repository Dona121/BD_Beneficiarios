from django.contrib import admin
from unfold.admin import ModelAdmin as UnfoldModelAdmin
from contenido import models
from unfold.admin import TabularInline

# Register your models here

@admin.register(models.CabezaFamilia)
class CabezaFamiliaAdmin(UnfoldModelAdmin):
    pass

@admin.register(models.Persona)
class PersonaAdmin(UnfoldModelAdmin):
    pass

@admin.register(models.InformacionGeografica)
class InfoGeograficaAdmin(UnfoldModelAdmin):
    list_display = ("codigo_dane_municipio",)