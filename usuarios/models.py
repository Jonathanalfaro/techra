from django.db import models
from django.contrib.auth.models import User

class Usuarios(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_techra = models.CharField(max_length=100)
    password_techra = models.CharField(max_length=100)

    def __str__(self):
        return self.user_techra



