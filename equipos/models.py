from django.db import models

# Create your models here.
class EquipoTechra(models.Model):

    numero_serie = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100, null=True, blank=True)
    a_color = models.BooleanField(default=False,  null=True)

    def __str__(self):
        return self.numero_serie
