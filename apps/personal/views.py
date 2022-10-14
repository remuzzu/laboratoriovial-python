from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.personal.forms import PersonalForm

# Create your views here.
def index(request):
    return render(request, 'personal/index.html')

def personal_edit(request):
    return render(request, 'personal/editar.html')

def personal_create(request):
    return render(request, 'personal/crear.html')

def form_personal(request):
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():
            #Crea y guarda un objeto de base de datos a partir de los datos vinculados al formulario
            form.save() 
            return redirect('personal: index')
    else:
        form = PersonalForm()
        
    return render(request, 'personal/form.html', {'form': form})