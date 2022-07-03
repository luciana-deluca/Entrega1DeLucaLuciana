from django.urls import path
from AppCoder import views  
   
urlpatterns = [  
   
    path('', views.inicio, name= 'Inicio'),
    path("hockeyFormulario", views.hockeyFormulario, name='HockeyFormulario'),
    path("futbolFormulario", views.futbolFormulario, name='FutbolFormulario'),
    path("rugbyFormulario", views.rugbyFormulario, name='RugbyFormulario'),
    path('buscar/', views.buscar, name='BuscarFutbol'),
 
 ]