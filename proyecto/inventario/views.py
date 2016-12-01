from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Ubicacion, Equipo, Tipo_Equipo, Estado, Lista_Incidencia, Lista_Atributo,Atributo,Incidencia
from django.core import serializers
from .tables import EquipoTable,UbicacionTable,IncidenciaTable
from django.contrib.auth import authenticate,login,logout
from .forms import IncidenciaForm
from django.shortcuts import redirect



def index(request):
    return render(request,'inventario/index.html',{})

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request,user)
        ...
    else:
            #
            ...

def logouth(request):
    logout(request)

def ubicacion(request, idUbicacion):
    ubicacion=Ubicacion.objects.get(pk=idUbicacion)
    print(ubicacion)
    equipos=Equipo.objects.filter(ubicacionEquipo=ubicacion)
    cantidadequipos = len(equipos)
    print (equipos)
    equipos = EquipoTable(equipos)
    return render(request,'inventario/ubicacion.html',{"ubicacion": ubicacion, "equipos": equipos, "cantidadequipos": cantidadequipos})

def ubicaciones(request):
    ubicaciones=Ubicacion.objects.all()
    ubicacions= UbicacionTable(ubicaciones)
    return render(request,'inventario/ubicaciones.html', {"ubicacions": ubicacions})

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
    incidencias=equipo.Incidencias.all()
    #print(equipo.Lista_Incidencia.all())
    #print (equipo.Incidencias.filter(idEquipo__idincidencias=idIncidencia))
    #Incidencia.objects.filter()
    #incidencias=Lista_Incidencia.objects.all().filter(idEquipo__id=idEquipo)
    atributos=Lista_Atributo.objects.all().filter(idEquipo__id=idEquipo)
    print(incidencias)
    listaincidencia=IncidenciaTable(incidencias)
    #print(atributos)
    return render(request,'inventario/equipo.html',{"equipo": equipo, "atributos":atributos, "listaincidencia":listaincidencia})

def incidencia_new(request):
    if request.method == "POST":
        form = IncidenciaForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('/inventario/')
        else:
            return redirect('/inventario/')
    else:
        form = IncidenciaForm()
        return render(request,'inventario/NuevaIncidencia.html',{'form':form})
