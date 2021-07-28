from django.db import models

# Create your models here.
class Arte(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)