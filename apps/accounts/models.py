from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class Lista_Pelicula(models.Model):
#     pelicula_id = models.CharField(max_length=50)
    
    
# class Lista(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50)
#     user = models.ManyToManyField(User)
#     peliculas = models.ManyToManyField(Lista_Pelicula)
    
    
# class Gusto(models.Model):
#     user = models.ManyToManyField(User)
#     genero_id = models.CharField(max_length=50)