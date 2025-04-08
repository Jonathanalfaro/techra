from django.db import models

# Create your models here.
class Refacciones(models.Model):
    id_ticket = models.IntegerField(blank=True, null=True)
    diagnostico_sol = models.CharField(max_length=255, blank=True, null=True)
    no_parte_componente = models.CharField(max_length=255, blank=True, null=True)
    tipo_componente = models.CharField(max_length=255, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    fecha_entrega = models.DateTimeField(blank=True, null=True)
    modelo =  models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.no_parte_componente}'

    class Meta:
        verbose_name_plural = 'Refacciones'
