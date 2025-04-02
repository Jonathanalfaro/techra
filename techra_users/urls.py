from . import views
from django.urls import include, path

urlpatterns = [
    path('usuarios/', views.techra_users_list, name='techra_users'),
]