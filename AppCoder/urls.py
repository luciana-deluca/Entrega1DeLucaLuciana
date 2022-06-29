from django.urls import path
from AppCoder import views  
   
urlpatterns = [  
   
    path('', views.inicio, name= 'Inicio'),
    path("hockey/", views.hockey, name= 'Hockey'),
    path("futbol/", views.futbol, name= 'Futbol'),
    path("rugby/", views.rugby, name= 'Rugby'),
    path('futbolFormulario', views.futbol, name= 'FutbolFormulario'), 
    path('buscar/', views.buscar), 
 
 ]