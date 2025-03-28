from django.db import models

# Create your models here.
class Localizacion(models.Model):

    id_usuario = models.IntegerField()
    latitud = models.FloatField()
    longitud = models.FloatField()
    nombre = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    id_puesto = models.IntegerField()
    id_ticket = models.IntegerField()
    id_estatus_ticket = models.IntegerField()
    fecha_hora = models.DateTimeField()
    porcentaje_bateria = models.IntegerField()