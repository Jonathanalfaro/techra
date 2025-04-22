
from .views import lista_localizaciones, lista_localizaciones_usuario, registrar_localizacion, get_map, mapa_localizaciones

from django.urls import path

urlpatterns = [
    path('localizaciones/',lista_localizaciones, name='lista_localizaciones'),
    path('localizaciones/<int:user_id>',lista_localizaciones_usuario, name='lista_localizaciones_usuario'),
    path('localizaciones/registrar',registrar_localizacion, name='registrar_localizacion'),
    path('localizaciones/mapa/<str:latitud>/<str:longitud>/',get_map, name='get_map'),
    path('localizaciones/mapa/<int:user_id>',mapa_localizaciones, name='mapa_localizaciones'),
]