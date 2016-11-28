from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Ubicacion, Equipo, Tipo_Equipo, Estado, Lista_Incidencia, Lista_Atributo,Atributo,Incidencia
from django.core import serializers
from .tables import EquipoTable

def index(request):
    return render(request,'inventario/index.html',{})

def ubicacion(request, idUbicacion):
    ubicacion=Ubicacion.objects.get(pk=idUbicacion)
    print(ubicacion)
    equipos=Equipo.objects.filter(ubicacionEquipo=ubicacion)
    print (equipos)
    equipos = EquipoTable(equipos)
    return render(request,'inventario/ubicacion.html',{"ubicacion": ubicacion, "equipos": equipos})

def ubicaciones(request):
    ubicaciones=Ubicacion.objects.all()
    return render(request,'inventario/ubicaciones.html', {"ubicaciones": ubicaciones})

def ubicaciones_json(request):
    ubicaciones=Ubicacion.objects.all()
    print (ubicaciones)
    return JsonResponse(serializers.serialize('json',ubicaciones,fields=("id")), safe=False)

def estado(request,idEstado):
    estado=Estado.objects.get(pk=idEstado)
    estadoequipo=Equipo.objets.filter(estadoEquipo=idEstado)
    return render(request,'inventario/equipo.html',{"estado":estado,"estadoequipo":estadoequipo})

def tipoequipo(request,idTipo_Equipo):
    tipoequipo=Tipo_Equipo.objects.get(pk=idTipo_Equipo)
    tipoEquipo=Tipo_Equipo.objets.filter(tipoEquipo=idTipo_Equipo)
    return render(request,'inventario/equipo.html',{"tipoequipo":tipoequipo, "tipoEquipo":tipoEquipo})

def equipo(request,idEquipo):
    equipo=Equipo.objects.get(pk=idEquipo)
    incidencias=Lista_Incidencia.objects.all().filter(idEquipo__id=idEquipo)
    print(incidencias)
    return render(request,'inventario/equipo.html',{"equipo": equipo,"incidencias":incidencias})


# def atributo(request, idAtributo):
#     atributo=Atributo.objects.get(pk=idAtributo)
#     nombreAtributo=Atributo.objects.filter(idEquipo=idAtributo)
#     return render(request,'inventario/equipo.html', {"atributo": atributo, "nombreAtributo":nombreAtributo,})
#
# def atributos(request):
#     atributos=Atributos.objects.all()
#     return render(request,'inventario/equipo.html', {"atributos": atributos})



# def listatributo(request,idEquipo,idAtributo):
#     atributo=Lista_Atributo.objects.get(pk=idAtributo)
#     equipo=Equipo.objects.get(pk=idEquipo)
#     valor=Lista_Atributo.objects.filter(idAtributo=idEquipo)
#     return render(request,'inventario/equipo.html',{"atributo": atributo, "equipo": equipo, "valor":valor})

# def tipoequipo(request,idTipo_Equipo):
