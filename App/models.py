from django.db import models

class Integrante(models.Model):
    nombre=models.CharField(max_length=40)
    relacion=models.CharField(max_length=40)
    edad=models.IntegerField()
    fecha=models.CharField(max_length=40)
