from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()
    nacionalidad=models.CharField(max_length=50)
    dni=models.IntegerField()