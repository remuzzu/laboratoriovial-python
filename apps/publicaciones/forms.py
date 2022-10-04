from django import forms
from apps.publicaciones.models import Congreso


class CongressForm(forms.forms):
   class Meta:
      model = Congreso
      
      field = [
         'anio',
         'lugar'
      ]
      labels = {
         'anio': 'Año',
         'lugar': 'Lugar',         
      }
      widgets = {
         'anio': forms.TextInput(attrs={'class': 'form-control'}),
         'lugar': forms.TextInput(attrs={'class': 'form-control'}),
      }
      
      # 'persona': forms.Select(attrs={'class': 'form-control'}),
      # 'vacuna': forms.CheckboxSelectMultiple()
   
      # anio = forms.CharField(label='año', max_length=4)
      # lugar = forms.CharField(label='lugar', max_length=200)
   