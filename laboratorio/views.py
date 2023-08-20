from django.shortcuts import render, HttpResponseRedirect
from .import views
from .models import Laboratorio,DirectorGeneral,Producto
from .forms import LabForm


def v_index(request):

    context = { 'laborat': Laboratorio.objects.all()
            }

    return render ( request, 'v_index.html', context )

    

def insertar(request):
    if request.method == "POST":
        datas = request.POST.copy()
        formcrear = LabForm(datas)
        if formcrear.is_valid():
            formcrear.save()
            return HttpResponseRedirect("/")
    context ={
        "form":LabForm(),
    }

    return render(request,'insertar.html',context)

def update(request,laboratorio_id):
    lab = Laboratorio.objects.get(id=laboratorio_id)

    if request.method == 'POST':
        datas = request.POST.copy()
        formedition = LabForm(datas, instance=lab)
        if formedition.is_valid:
            formedition.save()
        return HttpResponseRedirect("/")
    else:

        context = {
        "formedition" : LabForm(instance=lab)
        }

        return render(request,'update.html',context)

def delete(request,laboratorio_id):
    if request.method == 'POST':
        Producto.objects.filter(laboratorio = laboratorio_id).delete()
        DirectorGeneral.objects.filter(laboratorio__id = laboratorio_id ).delete()
        Laboratorio.objects.get(id=laboratorio_id).delete()
        return HttpResponseRedirect('/')

    context = {'lab': Laboratorio.objects.get(id=laboratorio_id)}

    return render(request,"delete.html",context)
    
    

    