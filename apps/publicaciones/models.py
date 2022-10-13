from django.db import models
from apps.personal.models import Persona
from django import forms

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
   
class CongressForm(forms.ModelForm):  
   class Meta:
      model = Congreso   
      fields = ['anio', 'lugar'] # Tiene que ir en el mismo orden que el modelo
      
      # El widget maneja la representación del HTML y la extracción de datos de un diccionario GET/POST que corresponde al widget.
      widgets = {
         'anio': forms.TextInput(attrs={'class': 'form-control'}),
         'lugar': forms.TextInput(attrs={'class': 'form-control'}),
      }
      labels = {
         'anio': 'Año',
         'lugar': 'Lugar',         
      }
   
  
class PublicacionForm(forms.ModelForm):
   class Meta:
      model = Publicacion
      fields = ['titulo', 'otrosAutores', 'congreso', 'autor']
      widgets = {
         'titulo': forms.TextInput(attrs={'class': 'form-control'}),
         'otrosAutores': forms.TextInput(attrs={'class': 'form-control'}),
         'congreso': forms.Select(attrs={'class': 'form-control'}),
         'autor': forms.CheckboxSelectMultiple(),
      }
      labels = {
         'titulo': 'Título',
         'otrosAutores': 'Otros Autores (no perteneciente al laboratorio vial)',
         'congreso': 'Congreso',
         'autor': 'Autores',
      }
      
   
   
   
