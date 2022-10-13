from django import forms
from apps.personal.models import Persona
from apps.publicaciones.models import Congreso

class CongressForm(forms.Form):  
   anio = forms.IntegerField(label='Año')
   lugar = forms.CharField(label='Lugar', max_length=200)

class PublicacionForm(forms.ModelForm):
   titulo = forms.CharField(max_length=200)
   otrosAutores = forms.CharField(max_length=200, required=False)
   congreso = forms.ModelChoiceField(queryset=Congreso.objects.all(), empty_label=None)
   #models.ForeignKey(Congreso, null=True, on_delete=models.CASCADE)
   autor = forms.ModelMultipleChoiceField(queryset=Persona.objects.all())
   
      