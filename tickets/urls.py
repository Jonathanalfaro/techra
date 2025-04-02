from . import views
from django.urls import include, path

urlpatterns = [
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('tickets/usuario/<str:user_id>', views.ticket_list_by_user, name='ticket_list_by_user'),
]