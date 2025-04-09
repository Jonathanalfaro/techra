from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    clave_cliente = models.IntegerField()


    def __str__(self):
        return self.nombre