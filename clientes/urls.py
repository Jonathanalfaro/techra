
from .views import lista_clientes, detalle_cliente

from django.urls import path

urlpatterns = [
    path('clientes/',lista_clientes, name='lista_clientes'),
    path('clientes/<str:cliente>',detalle_cliente, name='detalle_cliente'),
]