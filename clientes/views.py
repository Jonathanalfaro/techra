import random

from django.shortcuts import render

from equipos.models import EquipoTechra
from techra_users.models import TechraUsers
from tickets.models import Ticket
from .models import Cliente
from api_techra.views import get_tickets_cliente_techra, get_refacciones_techra
import json
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
    # tickets = Ticket.objects.filter(clave_cliente=cliente[0].clave_cliente)
    try:
        tickets_techra = get_tickets_cliente_techra(request, cliente[0].clave_cliente)
        tickets_techra = json.loads(tickets_techra.content.decode("utf-8"))
    except Exception as e:
        tickets_techra = []
    for ticket in tickets_techra:
        if not Ticket.objects.filter(ticket=ticket['Ticket']).exists():
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
            if nuevo_ticket.serie:
                equipos_list = nuevo_ticket.serie.split(',')
                for equ in equipos_list:
                    equipo = EquipoTechra.objects.filter(numero_serie=equ.strip())
                    if not equipo:
                        equipo = EquipoTechra.objects.create(
                            numero_serie=equ.strip()
                        )
                        equipo.save()
        techra_user = TechraUsers.objects.filter(nombre=ticket['Tecnico'])
        if not techra_user:
            techra_user = TechraUsers.objects.create(
                id_usuario=random.randint(1000, 10000),
                nombre=ticket['Tecnico'],
            )
            techra_user.save()
    tickets = Ticket.objects.filter(clave_cliente=cliente[0].clave_cliente)
    lista_refacciones = []
    series = []
    for ticket in tickets:
        try:
            series_ticket = ticket.serie.split(',')
            series += series_ticket
        except:
            pass
    series = list(set(series))
    for serie in series:
        if serie != '':
            try:
                refacciones_techra = get_refacciones_techra(request, serie)
                refacciones_techra = json.loads(refacciones_techra.content.decode("utf-8"))
                lista_refacciones += refacciones_techra
            except:
                pass
    return render(request, 'detalle_cliente.html', {'cliente': cliente[0], 'tickets':tickets, 'refacciones': lista_refacciones})
