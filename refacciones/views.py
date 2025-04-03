from django.contrib.auth.decorators import login_required
from django.shortcuts import render



# Create your views here.
@login_required(login_url='login')
def refacciones_list_by_equipo(request, numero_serie):
    # refacciones = Refacciones.objects.all()
    refacciones = []
    return render(request, 'refacciones.html', {'refacciones': refacciones})