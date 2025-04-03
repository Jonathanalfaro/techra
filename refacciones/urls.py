from . import views
from django.urls import include, path

urlpatterns = [
    path('refacciones/equipo/<str:numero_serie>', views.refacciones_list_by_equipo, name='refacciones_list_by_equipo'),
]