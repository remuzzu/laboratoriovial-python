from distutils.command.upload import upload
from django.db import models
from django import forms

# Le dicen a Django: "Este texto debe traducirse al idioma del usuario final
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Persona(models.Model):
   id = models.AutoField(primary_key=True)
   nombre = models.CharField(max_length=50, verbose_name='Nombre')
   #descripcion = models.CharField(max_length=200, blank=True)
   # verbose_name informa al usuario como se llama ese campo
   descripcion = models.TextField(null=True, verbose_name='Descripción')
   imagen = models.ImageField(upload_to = 'imagenes/', null=True, verbose_name='Imágen')
   
   def __str__(self) -> str:
      return '{} - {}'.format(self.nombre, self.descripcion)

class PersonalForm(forms.ModelForm):
   class Meta:
      model = Persona
      fields = ['nombre']
      widgets = {
         'nombre': forms.TextInput(attrs={'class': 'form-control'})
      }
      labels = {
         'nombre': _('Nombre'),
      }
      help_texts = {
         'name': _('Ingrese el nombre del personal del laboratorio vial.'),
      }
      error_messages = {
         'name': {
               'max_length': _("El nombre NO debe superar los 50 caracteres."),
         },
      }