from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.publicaciones.forms import CongressForm, PublicacionForm

# Create your views here.
def index_publicaciones(request):
    return render(request, 'publicaciones/index.html')

def new_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('publicaciones: index')
    else:
        form = PublicacionForm()
        
    return render(request, 'publicaciones/new.html', {'form': form})

def new_congress(request):
    if request.method == 'POST':
        form = CongressForm(request.POST)
        if form.is_valid():
            #Crea y guarda un objeto de base de datos a partir de los datos vinculados al formulario
            form.save() 
            return redirect('publicaciones: index')
    else:
        form = CongressForm()
        
    return render(request, 'publicaciones/new_congress.html', {'form': form})