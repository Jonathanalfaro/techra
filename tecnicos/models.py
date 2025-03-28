from django.db import models

# Create your models here.
class Tecnico(models.Model):

    nombre = models.CharField(max_length=100)
    id_techra = models.IntegerField()

    def __str__(self):
        return self.nombre
