from django.db import models


class Autor(models.Model):
    nombre = models.CharField('Nombres', max_length=50)
    nacionalidad = models.CharField(blank=True, max_length=25)

    def __str__(self):
        return self.nombre
 
class Libros(models.Model):
    title = models.CharField('titulo', blank=False, max_length=150)
    resume = models.TextField('Resumen', blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.title