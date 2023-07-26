from django.db import models

# Create your models here.

class data_user(models.Model):
    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre + f" dni: {self.dni}"