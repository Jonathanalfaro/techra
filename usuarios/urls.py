
from .views import LoginApp,  LogoutApp,  profile_view

from django.urls import path

urlpatterns = [
    path('login/',LoginApp, name='login'),
    path('logout/',LogoutApp, name='logoout'),
    path('perfil/',profile_view, name='profile')
]