import json

from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from zeep import Client

# Create your views here.
def get_tickets_techra(request):
    tickets = None
    base_url  = settings.BASE_URL
    ws_name = settings.WS_NAMES['tickets']
    url = f'{base_url}{ws_name}'
    cliente_tickets = Client(url)
    res = cliente_tickets.service.getTickets(
        'Ib-lGGWrv=Mmhqx',
        '',  # usuario
        '',  # status
        '2025-03-01',  # fecha
        '',  # fechafin
        '',  # latitud
        '',  # longitud
        '',  # pagina
        '',  # tampagina
        '',  # ticket
        '',  # serie
        0,  # cerrados
        0,  # cancelados
        0,  # morosos
        '',  # tipo
        '',  # cliente
        ''  # todos
    )
    res = json.loads(res)
    return JsonResponse(res, safe=False)