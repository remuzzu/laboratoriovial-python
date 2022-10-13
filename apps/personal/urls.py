from django.urls import path
from  .views import (
    index,
    new_personal
)

urlpatterns = [
    path("", index, name='personal-index'),    # Cuando esta vacio, por defecto entraria al index del personal
    path("new", new_personal), # Los name los vamos a usar mucho en las templates
]