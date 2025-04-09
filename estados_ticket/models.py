from django.db import models

# Create your models here.
class EstadoTicket(models.Model):

    id_estado = models.IntegerField(primary_key=True)
    nombre_estado = models.CharField(max_length=255)