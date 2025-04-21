
from .views import lista_notas

from django.urls import path

urlpatterns = [
    path('notas/<str:ticket>',lista_notas, name='lista_notas'),
]