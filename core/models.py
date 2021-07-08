from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Genero(models.Model):
    nombre=models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

class Manga(models.Model):
    nombre = models.CharField(max_length=200)
    genero = models.ForeignKey(Genero, on_delete=CASCADE)
    anio = models.IntegerField()
    tomos = models.IntegerField()
    editorial = models.CharField(max_length=200)
    sinopsis = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre