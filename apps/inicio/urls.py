from django.urls import path
from apps.inicio.views import index

urlpatterns = [
    path("", index, name='inicio'),
]