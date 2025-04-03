from . import views
from django.urls import include, path

urlpatterns = [
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('tickets/usuario/<str:nombre_tecnico>', views.ticket_list_by_user, name='ticket_list_by_user'),
    path('tickets/equipo/<str:numero_serie>', views.ticket_list_by_equipo, name='ticket_list_by_equipo'),
]