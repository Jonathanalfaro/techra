import json
import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from api_techra.views import get_tickets_techra
from equipos.models import EquipoTechra
from techra_users.models import TechraUsers
from .models import Ticket


# Create your views here.
@login_required(login_url='login')
def ticket_list(request):
    tickets = Ticket.objects.all().order_by('ticket')
    if not tickets:
        try:
            tickets = get_tickets_techra(request)
            tickets = json.loads(tickets.content.decode("utf-8"))
            for ticket in tickets:
                nuevo_ticket = Ticket.objects.create(
                    ticket=ticket['Ticket'],
                    titulo=ticket['Titulo'],
                    fecha_creacion=ticket['FechaCreacion'],
                    prioridad=ticket['Prioridad'],
                    zona=ticket['Zona'],
                    tecnico=ticket['Tecnico'],
                    area_atencion=ticket['AreaAtencion'],
                    serie=ticket['Serie'],
                    clave_cliente=ticket['ClaveCliente'],
                    cliente=ticket['Cliente'],
                    localidad=ticket['Localidad'],
                    direccion=ticket['Direccion'],
                    contacto_1_nombre=ticket['Contacto1Nombre'],
                    contacto_1_email=ticket['Contacto1Email'],
                    contacto_1_telefono=ticket['Contacto1Telefono'],
                    contacto_2_nombre=ticket['Contacto2Nombre'],
                    contacto_2_email=ticket['Contacto2Email'],
                    contacto_2_telefono=ticket['Contacto2Telefono'],
                    latitud=ticket['Latitud'],
                    longitud=ticket['Longitud'],
                    distancia=ticket['Distancia'],
                    fecha_nota=ticket['FechaNota'],
                    id_tipo_prioridad=ticket['IdTipoPrioridad'],
                    tipo_prioridad=ticket['TipoPrioridad'],
                    id_color=ticket['IdColor'],
                    color=ticket['Color'],
                    minutos_alertamiento=ticket['MinutosAlertamiento'],
                    id_puesto_escalamiento=ticket['IdPuestoEscalamiento'],
                    mensaje_alerta=ticket['MensajeAlerta'],
                    alertar_despues_fecha=ticket['AlertarDespuesFecha'],
                    estatus_nota_alertamiento=ticket['EstatusNotaAlertamiento'],
                    tiempo_duracion=ticket['TiempoDuracion'],
                    unidad_medida_duracion=ticket['UnidadMedidaDuracion'],
                    fecha_hora_inicio=ticket['FechaHoraInicio'],
                    check_in=ticket['CheckIn'],
                    check_out=ticket['CheckOut'],
                    check_in_programado=ticket['CheckInProgramado'],
                    check_out_programado=ticket['CheckOutProgramado'],
                    id_ultimo_estado=ticket['IdUltimoEstado']
                )
                nuevo_ticket.save()
                techra_user = TechraUsers.objects.filter(nombre=ticket['Tecnico'])
                if not techra_user:
                    techra_user = TechraUsers.objects.create(
                        id_usuario=random.randint(1000, 10000),
                        nombre=ticket['Tecnico'],
                    )
                    techra_user.save()
                if nuevo_ticket.serie:
                    equipos_list = nuevo_ticket.serie.split(',')
                    for equ in equipos_list:
                        equipo = EquipoTechra.objects.filter(numero_serie=equ.strip())
                        if not equipo:
                            equipo = EquipoTechra.objects.create(
                                numero_serie=equ.strip()
                            )
                            equipo.save()

        except Exception as e:
            tickets = []
    return render(request, 'tickets.html', {'tickets': tickets})


@login_required(login_url='login')
def ticket_list_by_user(request, nombre_tecnico):
    tickets = Ticket.objects.filter(tecnico=nombre_tecnico)
    return render(request, 'tickets.html', {'tickets': tickets})


@login_required(login_url='login')
def ticket_list_by_equipo(request, numero_serie):
    tickets = Ticket.objects.filter(serie__contains=numero_serie)
    return render(request, 'tickets.html', {'tickets': tickets})
