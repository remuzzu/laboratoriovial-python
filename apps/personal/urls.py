from django.urls import path
from  .views import (
    index_personal
)

urlpatterns = [
    path("", index_personal),
]