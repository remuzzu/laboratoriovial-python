from django import forms
from apps.personal.models import Persona

class PersonalForm(forms.Form):
   nombre = forms.CharField(max_length=50)