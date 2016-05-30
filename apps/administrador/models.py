from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Lista(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    usuario_username = models.ForeignKey(User)

    
class Gusto(models.Model):
    usuario_username = models.ForeignKey(User)
    genero_id = models.CharField(max_length=50)
    

class Calificacion(models.Model):
    usuario_username = models.ForeignKey(User)
    pelicula_id = models.CharField(max_length=50)
    

class Lista_Pelicula(models.Model):
    lista_id = models.ForeignKey(Lista)
    pelicula_id = models.CharField(max_length=50)