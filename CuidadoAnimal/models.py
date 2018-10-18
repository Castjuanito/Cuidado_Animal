from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    cedula = models.IntegerField(max_length=12)
    password: str = models.CharField(max_length=1000)


class MedicoVeterinario(Usuario):
    especialidad = models.CharField(max_length=20)


class DuenoMascota(Usuario):
    direccion = models.CharField(max_length=30)
    telefono = models.IntegerField(max_length=12)
    correo = models.CharField(max_length=30)


class Mascota(models.Model):
    nombre = models.CharField(max_length=20)
    especie = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    fechaNacimiento = models.DateField()
    GENEROS = (
        ('H', 'Hombre'),
        ('M', 'Mujer'),
        ('O', 'Otro'),
    )
    genero = models.CharField(max_length=1, choices=GENEROS)
    color = models.CharField(max_length=10)
    edad = models.IntegerField(max_length=3)
