from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Calificacion(models.Model):
    pelicula_id = models.CharField(max_length=50)
    calificacion = models.PositiveIntegerField()
    user = models.ManyToManyField(User)

class Lista(models.Model):
    lista_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    user = models.ManyToManyField(User)
        
class ListaPeliculas(models.Model):
    pelicula_id = models.CharField(max_length=50)
    lista = models.ManyToManyField(Lista)
