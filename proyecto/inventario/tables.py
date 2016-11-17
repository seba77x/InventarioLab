from models import *
from table import Table
from table.columns import Column

class PostTable(Table):
    id = Column(field='id', header=u'Id')
    title = Column(field='title', header=u'Titulo')
    url = Column(field='url', header=u'Url')
    content = Column(field='content', header=u'Content')
    class Meta:
        model = Post
