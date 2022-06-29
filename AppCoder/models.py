from django.db import models

class Hockey(models.Model):
    club = models.CharField(max_length=30)
    integrantes = models.IntegerField()
    creacion = models.DateField()

class Futbol(models.Model):
    club = models.CharField(max_length=30)
    integrantes = models.IntegerField()
    emailclub = models.EmailField()

class Rugby(models.Model):
    club = models.CharField(max_length=30)
    integrantes = models.IntegerField()
    creacion = models.DateField()
    
