
from .views import lista_clientes

from django.urls import path

urlpatterns = [
    path('clientes/',lista_clientes, name='lista_clientes'),
]