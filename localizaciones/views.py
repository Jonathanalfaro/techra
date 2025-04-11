from django.shortcuts import render, redirect

from localizaciones.forms import CreateLocalizacion
from localizaciones.models import Localizacion


# Create your views here.
def lista_localizaciones(request):
    localizaciones = Localizacion.objects.all()
    return render(request, 'localizaciones.html', {'localizaciones': localizaciones})

def lista_localizaciones_usuario(request, user_id):
    localizaciones = Localizacion.objects.filter(user_id=user_id)
    return render(request, 'localizaciones.html', {'localizaciones': localizaciones})


def registrar_localizacion(request):
    if request.method == 'POST':
        form = CreateLocalizacion(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('/localizaciones/')
    else:
        form = CreateLocalizacion()
        form.fields['user_id'].initial = request.user.usuarios
    return render(request, 'registrar_localizacion.html', {'form': form})
