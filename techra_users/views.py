from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import TechraUsers

from tickets.models import Ticket
@login_required(login_url='login')
def techra_users_list(request):
    techra_users = TechraUsers.objects.all()
    # if not techra_users:
    #     print("No se encontraron usuarios en la base de datos.")
    #     techra_user = TechraUsers(id_usuario=1, nombre='John Doe')
    #     techra_user.save()
    for techra_user in techra_users:
        techra_user.numero_tickets = Ticket.objects.filter(tecnico=techra_user.nombre).count()
    return render(request, 'techra_users.html', {'techra_users': techra_users})

def detalle_techra_user(request, nombre_usuario):
    techra_user = {
        'nombre': nombre_usuario
    }
    tickets = Ticket.objects.filter(tecnico=nombre_usuario)
    return render(request, 'detalle_techra_user.html', {'techra_user': techra_user, 'tickets': tickets})
