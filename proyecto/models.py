from django.db import models

class Ubicacion(models.Model):
    nombreSala = models.CharField(max_length=10)
    piso = models.IntegerField
    tipoUbicacion = models.CharField(max_length=20)

    def __str__(self):
        return self.nombreSala

class Estado(models.Model):
    estado = models.CharField(max_length=10)

    def __str__(self):
        return self.estado

class Tipo_Equipo(models.Model):
    nombreTipo = models.CharField(max_length=20)

    def __str__(self):
        return self.nombreTipo

class Equipo(models.Model):
    ubicacionEquipo = models.ForeignKey(Ubicacion)
    estadoEquipo = models.ForeignKey(Estado)
    tipoEquipo = models.ForeignKey(Tipo_Equipo)

    def __str__(self):                                             # hacer lo mismo con las demas
        return self.tipoEquipo

class Atributo(models.Model):
    nombreAtributo = models.CharField(max_length=20)

    def __str__(self):
        return self.nombreAtributo

class Lista_Atributo(models.Model):
    idEquipo = models.ForeignKey(Equipo)
    idAtributo = models.ForeignKey(Atributo)
    valor = models.CharField(max_length=30)

    class Meta:
        unique_together=(("idEquipo","idAtributo"))

class Incidencia(models.Model):
    fechaInicio = models.DateField
    fechaTermino = models.DateField
    responsable = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=500)

    def __str__(self):                                             # hacer lo mismo con las demas
        return self.nombre

class Lista_Incidencia(models.Model):
    idEquipo = models.ForeignKey(Equipo)
    idIncidencia = models.ForeignKey(Incidencia)

    class Meta:
        unique_together=(("idEquipo","idIncidencia"))
