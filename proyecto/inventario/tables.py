
from .models import *
from table import Table
from table.columns import Column

class EquipoTable(Table):
    id = Column(field='id', header=u'Id')
    nombreEquipo= Column(field='nombreEquipo', header=u'Nombre Equipo')
    ubicacionEquipo = Column(field='ubicacionEquipo', header=u'Ubicacion')
    estadoEquipo = Column(field='estadoEquipo', header=u'Estado')
    tipoEquipo = Column(field='tipoEquipo', header=u'Tipo')

class UbicacionTable(Table):
    nombreSala= Column(field='nombreSala', header=u'Nombre Ubicacion')
    tipoUbicacion=Column(field='tipoUbicacion', header=u'Tipo Ubicacion')

class IncidenciaTable(Table):
    id= Column(field='id', header=u'Id')
    nombre= Column(field='nombre', header=u'Nombre')
    fechaInicio= Column(field='fechaInicio', header=u'Fecha Inicio')
    fechaTermino= Column(field='fechaTermino', header=u'Fecha Termino')
    descripcion= Column(field='descripcion', header=u'Descripcion')
    responsable= Column(field='responsable', header=u'Responsable')
