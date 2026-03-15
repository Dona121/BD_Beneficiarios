from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
    
class InformacionGeografica(models.Model):
    codigo_dane_municipio = models.CharField(max_length=5, verbose_name="Código DANE Municipio")
    nombre_municipio = models.CharField(max_length=50, verbose_name="Nombre Municipio")
    codigo_dane_centro_poblado = models.CharField(max_length=8, verbose_name="Código DANE Centro Poblado")
    nombre_centro_poblado = models.CharField(max_length=100, verbose_name="Nombre Centro Poblado")
    barrio = models.CharField(max_length=50, verbose_name="Nombre del Barrio", null=True,blank=True)
    longitud = models.DecimalField(max_digits=8,decimal_places=6)
    latitud = models.DecimalField(max_digits=8,decimal_places=6)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    class Meta:
        verbose_name = "Información Geográfica de la Persona"
        verbose_name_plural = "Información Geográfica de las Personas"

    def __str__(self):
        return f"{self.codigo_dane_municipio} - {self.nombre_municipio}"

class PersonaBase(models.Model):
    cedula = models.CharField(max_length=15,verbose_name="Cédula de ciudadanía",unique=True)
    primer_nombre = models.CharField(max_length=30,verbose_name="Primer Nombre")
    segundo_nombre = models.CharField(max_length=30,verbose_name="Segundo Nombre",null=True,blank=True)
    primer_apellido = models.CharField(max_length=30, verbose_name="Primer Apellido")
    segundo_apellido = models.CharField(max_length=30, verbose_name="Segundo Apellido")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        abstract = True

    def __str__(self):
        return f"{self.primer_nombre} {self.primer_apellido}"

class CabezaFamilia(PersonaBase):
    es_cabeza_de_familia = models.BooleanField()

    class Meta:
        verbose_name = "Cabeza Familia"
        verbose_name_plural = "Cabezas de Familia"
    
    def __str__(self):
        return f"{self.es_cabeza_de_familia}"
    
class Persona(PersonaBase):
    tipo_familiar = models.CharField(max_length=20,null=True)
    informacion_geografica = models.OneToOneField(
        InformacionGeografica,
        on_delete=models.CASCADE,
        null=True
    )
    cabeza_familia = models.ForeignKey(
        CabezaFamilia,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.tipo_familiar}"