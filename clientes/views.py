from django.shortcuts import render
from .models import Cliente
# Create your views here.

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html',{'clientes':clientes})


def detalle_cliente(request, cliente):
    cliente = Cliente.objects.filter(clave_cliente=cliente)
    return render(request, 'detalle_cliente.html', {'cliente': cliente})
