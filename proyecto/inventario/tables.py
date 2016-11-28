from .models import *
from table import Table
from table.columns import Column

class EquipoTable(Table):
    id = Column(field='id', header=u'Id')
    ubicacionEquipo = Column(field='ubicacionEquipo', header=u'Ubicacion')
    estadoEquipo = Column(field='estadoEquipo', header=u'Estado')
    tipoEquipo = Column(field='tipoEquipo', header=u'Tipo')
