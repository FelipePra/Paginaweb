from django.db import models

# Create your models here.
class Manga(models.Model):
    nombre = models.CharField(max_length=100)
    Demografia = models.CharField(max_length=50)
    Autor = models.CharField(max_length=100)
    Genero = models.CharField(max_length=50)
    Link = models.CharField(max_length=200)
    Sinopsis = models.CharField(max_length=200)
    Volumenes = models.CharField(max_length=50)
    Capitulos = models.CharField(max_length=50)
    Categoria = models.CharField(max_length=50)
    observacion = models.CharField(max_length=100,null=True)

class Demografia(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self) :
        return self.nombre
    class Meta:
        db_table = 'demografia'

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self) :
        return self.nombre
    class Meta:
        db_table = 'categoria'

class Genero(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self) :
        return self.nombre
    class Meta:
        db_table = 'genero'

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    Demografia = models.CharField(max_length=50)
    Autor = models.CharField(max_length=100)
    Genero = models.CharField(max_length=50)
    Link = models.CharField(max_length=200)
    Sinopsis = models.CharField(max_length=200)
    Volumenes = models.CharField(max_length=50)
    Capitulos = models.CharField(max_length=50)
    Categoria = models.CharField(max_length=50)
    observacion = models.CharField(max_length=100,null=True)
    class Meta:
        db_table = 'producto'