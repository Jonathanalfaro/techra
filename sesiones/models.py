from django.db import models


# Create your models here.
class SessionTechra(models.Model):
    fecha_creacion = models.DateTimeField()
    id_session = models.CharField(max_length=100)
    duracion_minutos = models.IntegerField()
    id_usuario = models.IntegerField()
    permiso_ep = models.IntegerField()
    id_empresa = models.IntegerField()
    id_puesto = models.IntegerField()
    minutos_monitoreo_anterior = models.IntegerField()
    minutos_monitoreo_posterior = models.IntegerField()
    UID = models.IntegerField()
