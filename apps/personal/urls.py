from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='personal_index'),    # Cuando esta vacio, por defecto entraria al index del personal
    path("crear", views.personal_create, name='personal_create'),    
    path("editar", views.personal_edit, name='personal_edit'),
]