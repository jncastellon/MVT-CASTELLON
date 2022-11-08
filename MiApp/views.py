from django.shortcuts import render
from MiApp.models import Familiares

def mostrar_familiares(request):
    
    primer_familiar = Familiares(nombre = 'Eduardo', apellido = 'Equis', edad = 60, fecha_de_nacimiento = '1960-06-17')
    segundo_familiar = Familiares(nombre = 'Luz', apellido = 'Belito', edad = 27, fecha_de_nacimiento = '1995-05-15')
    tercer_familiar = Familiares(nombre = 'Juan', apellido = 'Riquelme', edad = 30, fecha_de_nacimiento = '1999-11-20')
    
    return render(request, 'MiApp/familiares.html', {'Familiares': [primer_familiar,segundo_familiar,tercer_familiar]})
# Create your views here.
