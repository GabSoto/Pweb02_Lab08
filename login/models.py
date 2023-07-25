from django.db import models

# Create your models here.

class data_user(models.Model):
    nombre = models.CharField(max_length=200)