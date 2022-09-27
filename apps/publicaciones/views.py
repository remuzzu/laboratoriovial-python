from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_publicaciones(request):
    return HttpResponse("Estoy en el index de las publicaciones")

def new_publicaciones(request):
    return HttpResponse("Estamos listos para agregar una nueva publicacion")

def new_Congreso(request):
    return HttpResponse("Estamos listos para agregar un nuevo congreso")
