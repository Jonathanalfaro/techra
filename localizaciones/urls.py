
from .views import lista_localizaciones, lista_localizaciones_usuario, registrar_localizacion

from django.urls import path

urlpatterns = [
    path('localizaciones/',lista_localizaciones, name='lista_localizaciones'),
    path('localizaciones/<int:user_id>',lista_localizaciones_usuario, name='lista_localizaciones_usuario'),
    path('localizaciones/registrar',registrar_localizacion, name='registrar_localizacion'),
]