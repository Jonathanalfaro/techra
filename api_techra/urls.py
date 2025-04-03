
from .views import get_tickets_techra

from django.urls import path

urlpatterns = [
    path('tickets_techra/',get_tickets_techra, name='lista_tickets_techra'),
]