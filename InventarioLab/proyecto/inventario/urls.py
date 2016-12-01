from django.conf.urls import *
from django.conf.urls.static import static


from . import views

urlpatterns = [
    url(r'ubicacion/(?P<idUbicacion>[0-9]+)$', views.ubicacion),
    url(r'ubicacion/', views.ubicaciones),
    url(r'ubicacion.json/', views.ubicaciones_json),
    url(r'equipo/(?P<idEquipo>[0-9]+)$', views.equipo),
    url(r'inventario/', views.index),
    url(r'^$', views.index)

    ]
