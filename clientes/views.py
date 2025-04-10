from django.shortcuts import render

from tickets.models import Ticket
from .models import Cliente
# Create your views here.

def lista_clientes(request):
    clientes = Cliente.objects.all()
    # if not clientes:
    #     tickets = Ticket.objects.all()
    #     for ticket in tickets:
    #         cliente = Cliente(nombre=ticket.cliente, clave_cliente=ticket.clave_cliente)
    #         if not Cliente.objects.filter(clave_cliente=cliente.clave_cliente).exists():
    #             cliente.save()
    #     clientes = Cliente.objects.all()
    return render(request, 'clientes.html',{'clientes':clientes})


def detalle_cliente(request, cliente):
    cliente = Cliente.objects.filter(clave_cliente=cliente)
    tickets = Ticket.objects.filter(clave_cliente=cliente[0].clave_cliente)
    return render(request, 'detalle_cliente.html', {'cliente': cliente[0], 'tickets':tickets})
