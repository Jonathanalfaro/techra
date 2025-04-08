import json

from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from zeep import Client
from sesiones.models import SessionTechra


def get_refacciones_techra(request,numero_serie):
    sesion_techra = SessionTechra.objects.filter(UID=request.user.id)
    if not sesion_techra:
        res_sesion = inicia_sesion_techra(request)
        sesion = json.loads(res_sesion.content.decode('utf-8'))
    else:
        sesion = sesion_techra[0]
    id_session = sesion.id_session
    base_url = settings.BASE_URL
    ws_name = settings.WS_NAMES['refacciones']
    url = f'{base_url}{ws_name}'
    cliente_refacciones = Client(url)
    res = cliente_refacciones.service.obtenerRefaccionPorEquipo(
        numero_serie,
        id_session
    )
    res = json.loads(res)
    return JsonResponse(res, safe=False)


# Create your views here.
def inicia_sesion_techra(request):
    base_url  = settings.BASE_URL
    ws_name = settings.WS_NAMES['login']
    url = f'{base_url}{ws_name}'
    cliente_inicia_sesion = Client(url)
    usuario = request.user.usuarios.user_techra
    password = request.user.usuarios.password_techra
    res = cliente_inicia_sesion.service.autenticaUsuario(
        usuario,
        password,
        ''
    )
    res = json.loads(res)[0]
    nueva_sesion = SessionTechra(
        fecha_creacion = res['FechaCreacion'],
        id_session = res['IdSession'],
        duracion_minutos = res['DuracionMinutos'],
        id_usuario = res['IdUsuario'],
        permiso_ep = res['PermisoEP'],
        id_empresa = res['IdEmpresa'],
        id_puesto = res['IdPuesto'],
        minutos_monitoreo_anterior = res['MinutosMonitoreoAnterior'],
        minutos_monitoreo_posterior = res['MinutosMonitoreoPosterior'],
        UID = request.user.id
    )
    nueva_sesion.save()
    return JsonResponse(res, safe=False)
def get_tickets_techra(request):
    tickets = None
    sesion_techra = SessionTechra.objects.filter(UID=request.user.id)
    if not sesion_techra:
        res_sesion = inicia_sesion_techra(request)
        sesion = json.loads(res_sesion.content.decode('utf-8'))
    else:
        sesion = sesion_techra[0]
    id_session = sesion.id_session
    base_url  = settings.BASE_URL
    ws_name = settings.WS_NAMES['tickets']
    url = f'{base_url}{ws_name}'
    cliente_tickets = Client(url)
    res = cliente_tickets.service.getTickets(
        id_session,
        '',  # usuario
        '',  # status
        '2025-03-08',  # fecha
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
    res = json.loads(res)[:-1]
    return JsonResponse(res, safe=False)