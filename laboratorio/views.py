from django.shortcuts import render
from .import views
from .models import Laboratorio,DirectorGeneral,Producto


def v_index(request):

    context =  Laboratorio.objects.all()
    


    return render ( request, 'v_index.html',{'laborat': context })

    

def insertar(request):
    return render(request,'insertar.html')

def update(request,laboratorio_id):
    return render(request,'update.html')

def delete(request,laboratorio_id):
    context = {}

    return render(request,'delete.html')