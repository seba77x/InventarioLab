from django.contrib import admin
from .models import *

entities=[Ubicacion,Estado,Tipo_Equipo,Equipo,Atributo,Lista_Atributo,Incidencia,Lista_Incidencia]
admin.site.register(entities)
