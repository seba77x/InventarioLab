from django.db import models

class Ubicacion(models.Model):
    nombreSala = models.CharField(max_length=10)
    piso = models.IntegerField
    tipoUbicacion = models.CharField(max_length=20)

    def __str__(self):                                             # hacer lo mismo con las demas
        return self.nombreSala

class Estado(models.Model):
    estado = models.CharField(max_length=10)

class Tipo_Equipo(models.Model):
    nombreTipo = models.CharField(max_length=20)

class Equipo(models.Model):
    ubicacionEquipo = models.ForeignKey(Ubicacion)
    estadoEquipo = models.ForeignKey(Estado)
    tipoEquipo = models.ForeignKey(Tipo_Equipo)

class Atributo(models.Model):
    nombreAtributo = models.CharField(max_length=20)

class Lista_Atributo(models.Model):
    idEquipo = models.ForeignKey(Equipo)
    idAtributo = models.ForeignKey(Atributo)
    valor = models.CharField(max_length=30)

    class Meta:
        unique_together=(("idEquipo","idAtributo"))                 # mezclar foraneas en un pk artificial :3

class Incidencia(models.Model):
    fechaInicio = models.DateField
    fechaTermino = models.DateField
    responsable = models.CharField(max_length=30)

class Lista_Incidencia(models.Model):
    idEquipo = models.ForeignKey(Equipo)
    idIncidencia = models.ForeignKey(Incidencia)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=500)

    class Meta:
        unique_together=(("idEquipo","idIncidencia"))
