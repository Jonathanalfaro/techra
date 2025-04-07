# from django.http import HttpResponse
from django.shortcuts import render

from equipos.models import EquipoTechra


def lista_equipos(request):
    equipos = EquipoTechra.objects.all()
    return render(request, 'equipos.html', {'equipos': equipos})

def detalle_equipo(request, numero_serie):
    equipo = EquipoTechra.objects.filter(numero_serie=numero_serie.strip())
    if not equipo:
        render(request, 'detalle_equipo.html', {'equipo': {}})
    return render(request, 'detalle_equipo.html', {'equipo': equipo[0]})

