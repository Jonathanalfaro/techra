# from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from equipos.models import EquipoTechra
from tickets.models import Ticket
import json

from api_techra.views import get_refacciones_techra


def lista_equipos(request):
    equipos = EquipoTechra.objects.all()
    for equipo in equipos:
        equipo.numero_tickets = Ticket.objects.filter(serie__contains=equipo.numero_serie.strip()).count()
    return render(request, 'equipos.html', {'equipos': equipos})

def detalle_equipo(request, numero_serie):
    equipo = EquipoTechra.objects.filter(numero_serie__contains=numero_serie.strip())
    tickets = Ticket.objects.filter(serie__contains=numero_serie.strip())
    resultado_refacciones =get_refacciones_techra(request, numero_serie)
    refacciones = json.loads(resultado_refacciones.content.decode('utf-8'))
    for refaccion in refacciones:
        try:
            refaccion['FechaEntrega'] = datetime.strptime(refaccion['FechaEntrega'], '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M:%S')
        except ValueError:
            pass
    if not equipo:
        render(request, 'detalle_equipo.html', {'equipo': {}})
    return render(request, 'detalle_equipo.html', {'equipo': equipo[0], 'tickets': tickets, 'refacciones': refacciones})

