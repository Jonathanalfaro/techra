from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class TechraUsers(models.Model):

    id_usuario = models.IntegerField()
    nombre = models.CharField(max_length=100)