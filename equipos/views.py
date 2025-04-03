# from django.http import HttpResponse
from django.shortcuts import render


def lista_equipos(request):
    equipos = [{
        'numero_serie': 'ABC123456',
        'modelo': 'KYOCERA'
    },{
        'numero_serie': 'ABC123456',
        'modelo': 'KYOCERA'
    }]
    return render(request, 'equipos.html', {'equipos': equipos})

