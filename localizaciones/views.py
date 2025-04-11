import folium
from django.http import HttpResponse, JsonResponse
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
    map = folium.Map(location=[19.316736, -99.0609408], zoom_start=10)
    folium.Marker([19.316736, -99.0609408]).add_to(map)
    map = map._repr_html_()
    return render(request, 'registrar_localizacion.html', {'form': form, 'map':map})


def get_map(request, latitud, longitud):
    map = folium.Map(location=[latitud, longitud], zoom_start=15)
    folium.Marker([latitud, longitud]).add_to(map)
    map = map._repr_html_()
    return JsonResponse(map,  safe=False)
    # return render(request, 'map.html', {'map': map})
