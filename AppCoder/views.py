from django.shortcuts import render
from AppCoder.forms import FutbolFormulario
from AppCoder.models import Hockey
from AppCoder.models import Futbol
from AppCoder.models import Rugby
from django.template import loader
from django.http import HttpResponse

def inicio(request):
    return render(request, 'AppCoder/inicio.html')



def hockey(request):
    return render(request, "AppCoder/hockey.html")



def rugby(request):
    return render(request, "AppCoder/rugby.html")

def futbol(request):

      if request.method == 'POST':

            miFormulario = FutbolFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  fuchi= Futbol (club=informacion['club'], integrantes=informacion['integrantes'],
                   emailclub=informacion['email']) 

                  fuchi.save()

                  return render(request, "AppProyectoFinal/inicio.html") 

      else: 

            miFormulario= FutbolFormulario()

      return render(request, "AppCoder/futbol.html", {"miFormulario":miFormulario})


def buscar(request):
    if request.GET['club']:
        club = request.GET['club']
        print(club)
        equipo = Hockey.objects.filter(club__icontains=club)
        print(equipo)
        return render(request, "AppCoder/inicio.html", {'equipo': equipo, 'club':club})
            
    else: 

	      respuesta = "No enviaste datos"
    return render(request,"AppCoder/inicio.html", {"respuesta":respuesta})