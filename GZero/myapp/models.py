from django.db import models

# Create your models here.

class Artista(models.Model):
    rut_Artista = models.CharField(primary_key=True, max_length=10)
    nombre_Artista = models.CharField(max_length= 100)
    Telefono = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.nombre_Artista), str(self.email)

class Arte(models.Model):
    id_Arte = models.AutoField(db_column='idArte', primary_key=True)
    titulo_Arte = models.CharField(max_length=100)
    descripcion_Arte = models.CharField(max_length=400)
    precio_Arte = models.CharField(max_length= 8)
    tecnica_Arte = models.CharField(max_length=20)


    def __str__(self):
        return str(self.titulo_Arte) + " " +(self.descripcion_Arte)