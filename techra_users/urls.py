from . import views
from django.urls import include, path

urlpatterns = [
    path('usuarios/', views.techra_users_list, name='techra_users'),
    path('usuarios/<str:nombre_usuario>', views.detalle_techra_user, name='detalle_techra_users'),
]