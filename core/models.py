from django.db import models

# Create your models here.

class Flor(models.Model):
    nombre = models.CharField(max_length=100)
    valor =models.IntegerField()
    descripcion = models.CharField(max_length=300)
    estado = models.CharField(max_length=20)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='flores',null=True)
    def __str__(self):
        return self.nombre