from django.urls import path
from  .views import (
    index_publicaciones,
    new_publicacion,
    new_congress
)

urlpatterns = [
    path("index", index_publicaciones),
    path("new", new_publicacion),
    path("new-congress", new_congress),
]