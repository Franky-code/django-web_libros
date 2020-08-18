from django.db import models


class Autor(models.Model):
    nombre = models.CharField('Nombres', max_length=50)
    nacionalidad = models.CharField(blank=True, max_length=25)

    def __str__(self):
        return self.nombre