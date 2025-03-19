from django.db import models

class Celulares(models.Model):
    Modelo = models.CharField(max_length=100)
    Marca = models.CharField(max_length=100)
    Descripcion = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Modelo
