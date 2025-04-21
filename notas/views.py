import random

from django.shortcuts import render

from equipos.models import EquipoTechra
from techra_users.models import TechraUsers
from tickets.models import Ticket
from api_techra.views import get_notas_techra
import json


def lista_notas(request, ticket):
    notas = get_notas_techra(request, ticket)
    notas = json.loads(notas.content.decode('utf-8'))
    return render(request,'notas.html', {'ticket': ticket, 'notas': notas})
