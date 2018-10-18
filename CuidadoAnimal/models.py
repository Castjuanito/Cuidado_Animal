from django.db import models


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