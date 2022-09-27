from django.urls import path
from  .views import (
    index_publicaciones,
    new_publicaciones,
    new_Congreso
)

urlpatterns = [
    path("index", index_publicaciones),
    path("create", new_publicaciones),
    path("create-congress", new_Congreso),
]