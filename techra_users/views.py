from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import TechraUsers

@login_required(login_url='login')
def techra_users_list(request):
    techra_users = TechraUsers.objects.all()
    # if not techra_users:
    #     print("No se encontraron usuarios en la base de datos.")
    #     techra_user = TechraUsers(id_usuario=1, nombre='John Doe')
    #     techra_user.save()
    return render(request, 'techra_users.html', {'techra_users': techra_users})

def detalle_techra_user(request, nombre_usuario):
    techra_user = {
        'id_usuario': 1000,
        'nombre': nombre_usuario
    }
    return render(request, 'detalle_techra_user.html', {'techra_user': techra_user})
