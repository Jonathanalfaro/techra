import json

from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from zeep import Client
from sesiones.models import SessionTechra
import datetime
import pytz

def get_tickets_cliente_techra(request, cliente):
    base_url = settings.BASE_URL
    ws_name = settings.WS_NAMES['tickets']
    url = f'{base_url}{ws_name}'
    sesion_techra = get_session_techra(request)
    id_session = sesion_techra.id_session
    cliente_tickets = Client(url)
    # cliente_tickets.settings.strict = False
    res = cliente_tickets.service.getTickets(
        id_session,
        '',
        '',  # status,
        '',  # fecha,
        '',  # fechafin,
        '',  # latitud,
        '',  # longitud,
        '',  # pagina,
        '',  # tampagina,
        '',  # ticket,
        '',  # serie,
        1,  # cerrados,
        1,  # cancelados,
        0,  # morosos,
        '',  # área de atencion
        '',  # tipo,
        cliente,  # cliente,
        ''  # todos,
    )
    res = json.loads(res)[:-1]
    return JsonResponse(res, safe=False)

def get_session_techra(request):
    sesion_techra = SessionTechra.objects.filter(UID=request.user.id)
    if not sesion_techra:
        res_sesion = inicia_sesion_techra(request)
        sesion = json.loads(res_sesion.content.decode('utf-8'))
        sesion_techra = SessionTechra(
            fecha_creacion=sesion['FechaCreacion'],
            id_session=sesion['IdSession'],
            duracion_minutos=sesion['DuracionMinutos'],
            id_usuario=sesion['IdUsuario'],
            permiso_ep=sesion['PermisoEP'],
            id_empresa=sesion['IdEmpresa'],
            id_puesto=sesion['IdPuesto'],
            minutos_monitoreo_anterior=sesion['MinutosMonitoreoAnterior'],
            minutos_monitoreo_posterior=sesion['MinutosMonitoreoPosterior'],
            UID=request.user.id
        )
        sesion_techra.save()
    else:
        sesion_techra = sesion_techra[0]
        expires_at = sesion_techra.fecha_creacion + datetime.timedelta(minutes=120)
        if expires_at.strftime('%d/%m/%Y %H:%M') < datetime.datetime.now(pytz.timezone('America/Mexico_City')).strftime('%d/%m/%Y %H:%M'):
            res_sesion = inicia_sesion_techra(request)
            sesion = json.loads(res_sesion.content.decode('utf-8'))
            sesion_techra.fecha_creacion = sesion['FechaCreacion']
            sesion_techra.id_session = sesion['IdSession']
            sesion_techra.duracion_minutos = sesion['DuracionMinutos']
            sesion_techra.save()
    return sesion_techra

def get_refacciones_techra(request,numero_serie):
    sesion_techra = get_session_techra(request)
    id_session = sesion_techra.id_session
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
    return JsonResponse(res, safe=False)
def get_tickets_techra(request):
    tickets = None
    fecha_inicio = ''
    fecha_fin = ''
    cliente = ''
    sesion_techra = get_session_techra(request)
    id_session = sesion_techra.id_session
    base_url  = settings.BASE_URL
    ws_name = settings.WS_NAMES['tickets']
    url = f'{base_url}{ws_name}'
    cliente_tickets = Client(url)
    res = cliente_tickets.service.getTickets(
        id_session,
        '',
        '',  # status,
        fecha_inicio,  # fecha,
        fecha_fin,  # fechafin,
        '',  # latitud,
        '',  # longitud,
        '',  # pagina,
        '',  # tampagina,
        '',  # ticket,
        '',  # serie,
        0,  # cerrados,
        0,  # cancelados,
        0,  # morosos,
        '',  # área de atencion
        '',  # tipo,
        cliente,  # cliente,
        ''  # todos,
    )
    res = json.loads(res)[:-1]
    return JsonResponse(res, safe=False)


def get_notas_techra(request, ticket):
    sesion_techra = get_session_techra(request)
    id_session = sesion_techra.id_session
    base_url = settings.BASE_URL
    ws_name = settings.WS_NAMES['notas']
    url = f'{base_url}{ws_name}'
    cliente_notas = Client(url)
    res = cliente_notas.service.getNotas(
        ticket,
        '',
        '',
        '',
        id_session
    )
    res = json.loads(res)
    return JsonResponse(res, safe=False)