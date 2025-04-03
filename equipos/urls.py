
from .views import lista_equipos, detalle_equipo

from django.urls import path

urlpatterns = [
    path('equipos/',lista_equipos, name='lista_equipos'),
    path('equipos/<str:numero_serie>',detalle_equipo, name='detalle_equipo'),
]