from django.db import models
from django.contrib.auth.models import User

# Modelo para los artistas
class Artista(models.Model):
    rut_artista = models.CharField(primary_key=True, max_length=10)
    nombre_artista = models.CharField(max_length=100)
    telefono = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_artista} ({self.email})"

# Modelo para las obras de arte
class Art(models.Model):
    art_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    style = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True)  # Asegúrate de que este campo exista

    def __str__(self):
        return self.art_name