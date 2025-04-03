from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Ticket


# Create your views here.
@login_required(login_url='login')
def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets.html', {'tickets': tickets})


@login_required(login_url='login')
def ticket_list_by_user(request, user_id):
    tickets = Ticket.objects.all()
    return render(request, 'tickets.html', {'tickets': tickets})


@login_required(login_url='login')
def ticket_list_by_equipo(request, equipo_id):
    tickets = Ticket.objects.all()
    return render(request, 'tickets.html', {'tickets': tickets})
