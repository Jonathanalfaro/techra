
from .views import lista_equipos

from django.urls import path

urlpatterns = [
    path('equipos/',lista_equipos, name='lista_equipos'),
]