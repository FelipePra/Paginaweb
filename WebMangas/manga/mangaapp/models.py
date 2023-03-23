from django.db import models

# Create your models here.

from django.urls import reverse

class Manga(models.Model):
    TIPOS_DE_MANGA = [
        ('manga', 'Manga'),
        ('manhua', 'Manhua'),
        ('manhwa', 'Manhwa'),
        ('webtoon', 'Webtoon'),
    ]

    nombre = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    demografia = models.CharField(max_length=100)
    cantidad_capitulos = models.IntegerField()
    fecha_publicacion = models.DateField()
    sinopsis = models.TextField()
    tipo = models.CharField(max_length=10, choices=TIPOS_DE_MANGA, default='manga')

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('detalle_manga', kwargs={'pk': self.pk})
