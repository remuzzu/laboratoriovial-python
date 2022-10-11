from django import forms
from apps.publicaciones.models import Congreso

class CongressForm(forms.ModelForm):
   
   class Meta:
      model = Congreso
      
      fields = ['anio', 'lugar'] # Tiene que ir en el mismo orden que el modelo
      # models.IntegerField()
      # models.CharField
   
      anio = forms.IntegerField(label='Año')
      lugar = forms.CharField(label='Lugar', max_length=200)
      
      labels = {
         'anio': 'Año',
         'lugar': 'Lugar',         
      }
      
      # El widget maneja la representación del HTML y la extracción de datos de un diccionario GET/POST que corresponde al widget.
      widgets = {
         'anio': forms.TextInput(attrs={'class': 'form-control'}),
         'lugar': forms.TextInput(attrs={'class': 'form-control'}),
      }
      
      # 'persona': forms.Select(attrs={'class': 'form-control'}),
      # 'vacuna': forms.CheckboxSelectMultiple()
   
      # anio = forms.CharField(label='año', max_length=4)
      # lugar = forms.CharField(label='lugar', max_length=200)
   