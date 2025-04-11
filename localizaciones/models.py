from django.contrib.auth.models import AbstractUser
from django.db import models

from usuarios.models import Usuarios


# Create your models here.
class Localizacion(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='localizaciones')

    def __str__(self):
        return f"{self.latitud}-{self.longitud}"
