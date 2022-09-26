from django.contrib import admin
from apps.publicaciones.models import Congreso, Publicacion

# Register your models here.
admin.site.register(Congreso)

admin.site.register(Publicacion)