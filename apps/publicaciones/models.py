from __future__ import annotations
from pyexpat import model
from django.db import models
from apps.personal.models import Persona

# Create your models here.
class Congreso(models.Model):
   anio = models.IntegerField()
   lugar = models.CharField(max_length=200)
   
   def __str__(self) -> str:
      return '{} - {}'.format(self.anio, self.lugar)
   
   
class Publicacion(models.Model):
   # id = models.AutoField(primary_key = True)
   # id no haria falta definirlo, porque por defecto django lo define tal cual como esta arriba
   titulo = models.CharField(max_length=200)
   otrosAutores = models.CharField(max_length=200, blank=True)
   congreso = models.ForeignKey(Congreso, null=True, on_delete=models.CASCADE)
   autor = models.ManyToManyField(Persona)
   
   

