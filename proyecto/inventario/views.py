from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Ubicacion, Equipo
from django.core import serializers


def index(request):
    return render(request,'inventario/index.html',{})

def ubicacion(request, idUbicacion):
    ubicacion=Ubicacion.objects.get(pk=idUbicacion)
    equipos=Equipo.objects.filter(ubicacionEquipo=ubicacion.id)
    print (equipos)
    return render(request,'inventario/ubicacion.html',{"ubicacion": ubicacion, "equipos": equipos})

def ubicaciones(request):
    ubicaciones=Ubicacion.objects.all()
    return render(request,'inventario/ubicaciones.html', {"ubicaciones": ubicaciones})

def ubicaciones_json(request):
    ubicaciones=Ubicacion.objects.all()
    print (ubicaciones)
    return JsonResponse(serializers.serialize('json',ubicaciones,fields=("id")), safe=False)

def equipo(request,idEquipo):
    return render(request,'inventario/equipo.html',{})
