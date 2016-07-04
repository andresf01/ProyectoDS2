from django.contrib import admin
from .models import Calificacion, Lista, ListaPeliculas

# Register your models here.
admin.site.register(Calificacion)
admin.site.register(Lista)
admin.site.register(ListaPeliculas)