from ctypes import c_longdouble
import email
from django.shortcuts import render
from AppCoder.models import Hockey
from AppCoder.models import Futbol
from AppCoder.models import Rugby
from django.template import loader
from django.http import HttpResponse
from AppCoder.forms import HockeyFormulario
from AppCoder.forms import FutbolFormulario
from AppCoder.forms import RugbyFormulario


def inicio(request):
    return render(request, 'AppCoder/inicio.html')


def hockey(request):
    return render(request, "AppCoder/hockey.html")


def rugby(request):
    return render(request, "AppCoder/rugby.html")
    

def futbol(request):
    return render(request, "AppCoder/futbol.html")


def hockeyFormulario(request):

    if request.method == 'POST':

        miFormulario1 = HockeyFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:

            informacion= miFormulario.cleaned_data

            hockey = Hockey(club=informacion['club'], integrantes=informacion['integrantes'], creacion=informacion['creacion'])
            hockey.save()

        return render(request, "AppCoder/inicio.html")

    else:

        miFormulario= HockeyFormulario()

    return render(request, "AppCoder/hockeyFormulario.html", {"miFormulario":miFormulario})





def futbolFormulario(request):

    if request.method == 'POST':

        miFormulario2 = FutbolFormulario(request.POST)
        print(miFormulario2)

        if miFormulario2.is_valid:

            informacion= miFormulario2.cleaned_data

            futbol = Futbol(club=informacion['club'], integrantes=informacion['integrantes'], emailclub=informacion['emailclub'])
            futbol.save()

        return render(request, "AppCoder/inicio.html")

    else:

        miFormulario2= FutbolFormulario()

    return render(request, "AppCoder/futbolFormulario.html", {"miFormulario2":miFormulario2})



    

def rugbyFormulario(request):

    if request.method == 'POST':

        miFormulario = RugbyFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:

            informacion= miFormulario.cleaned_data

            rugby = Rugby(club=informacion['club'], integrantes=informacion['integrantes'], creacion=informacion['creacion'])
            rugby.save()

        return render(request, "AppCoder/inicio.html")

    else:

        miFormulario= RugbyFormulario()

    return render(request, "AppCoder/rugbyFormulario.html", {"miFormulario":miFormulario})   


def buscar(request):

    if  request.GET["club"]:
 
        club = request.GET['club'] 
        print(club)
        clubes = Futbol.objects.filter(club__icontains=club)
        print(clubes)
        return render(request, "AppCoder/buscar.html", {"Info":club, "Club":clubes})

    else: 

        respuesta =  "No enviaste datos"
        
        return render(request,"ProyectoCoderApp/inicio.html",{"respuesta":respuesta})


    