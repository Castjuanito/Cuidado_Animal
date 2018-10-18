from typing import Any

from django.db import models


class Fruta(models.Model):
    nombre = models.CharField(max_length=30)

class CentroVeterinario(models.Model):

    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    horaA = models.DateTimeField()
    horaC = models.DateField()


class Servicio(models.Model):

    detalle = models.CharField(max_length=30)
    centroVeterinario = models.ForeignKey(CentroVeterinario, on_delete=models.CASCADE)


class PalabraClave(models.Model):

    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    palabra  = models.CharField(max_length=30)


class AdminostradorCentroVeterinario(models.Model):

    nombreUsuario = models.CharField(max_length=30)
    password = models.CharField(max_length=1000)
    centroVeterinario = models.OneToOneField(
        CentroVeterinario,
        on_delete=models.CASCADE,
        primary_key=True,
    )


# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    cedula = models.IntegerField
    password = models.CharField(max_length=1000)  # type: Any


class MedicoVeterinario(Usuario):
    especialidad = models.CharField(max_length=20)


class DuenoMascota(Usuario):
    direccion = models.CharField(max_length=30)
    telefono = models.IntegerField
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
    edad = models.IntegerField
    dueno = models.ForeignKey(
        DuenoMascota,
        on_delete=models.CASCADE,
    )

class Calificacion(models.Model):
    calificacion = models.IntegerField
    dueno = models.ForeignKey(DuenoMascota,
                              on_delete=models.CASCADE)
    cVeterinario = models.OneToOneField(CentroVeterinario,
                                        on_delete=models.CASCADE)


class HistoriaClinica(models.Model):
    mascota = models.ForeignKey(
        Mascota,
        on_delete=models.CASCADE,
    )


class Casos(models.Model):
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    descripcion = models.TextField(max_length=1000)
    hClinica = models.ForeignKey(
        HistoriaClinica,
        on_delete=models.CASCADE,
    )


class DescripcionCosto(models.Model):
    costo = models.FloatField(max_length=10)
    descripcion = models.CharField(max_length=30)
    casos = models.OneToOneField(
        Casos,
        on_delete=models.CASCADE,
        primary_key=True,
    )
