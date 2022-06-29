from django import forms

class Hockey(forms.Form):
    club = forms.CharField(max_length=30)
    integrantes = forms.IntegerField()
    creacion = forms.DateField()

class FutbolFormulario(forms.Form):
    club = forms.CharField(max_length=30)
    integrantes = forms.IntegerField()
    emailclub = forms.EmailField()

class Rugby(forms.Form):
    club = forms.CharField(max_length=30)
    integrantes = forms.IntegerField()
    creacion = forms.DateField()