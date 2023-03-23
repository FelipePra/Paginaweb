from django.db import models

# Create your models here.


class Manga(models.Model):
    nombre = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='fotos_manga')
    demografia = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    link = models.URLField()
    sinopsis = models.TextField()
    cantidad_volumenes = models.IntegerField()
    cantidad_capitulos = models.IntegerField()
