
from .views import get_tickets_techra,inicia_sesion_techra, get_refacciones_techra

from django.urls import path

urlpatterns = [
    path('tickets_techra/',get_tickets_techra, name='lista_tickets_techra'),
    path('sesion_techra/',inicia_sesion_techra, name='inicia_sesion_techra'),
    path('refacciones_techra/<str:numero_serie>',get_refacciones_techra, name='refacciones_techra'),
]