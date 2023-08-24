from django.shortcuts import render, HttpResponseRedirect
from .import views
from .models import Laboratorio,DirectorGeneral,Producto
from .forms import LabForm
import sweetify

def v_index(request):

    if 'numveces' in request.session:
        num = request.session["numveces"] #se obtiene la variable de sesion
    else:
        num = 0

    request.session['numveces'] = num + 1


    context = { 
        'numveces': request.session['numveces'],
        'laborat': Laboratorio.objects.all()
            }

    return render ( request, 'v_index.html', context )

    

def insertar(request):
    if request.method == "POST":
        datas = request.POST.copy()
        formcrear = LabForm(datas)
        if formcrear.is_valid():
            formcrear.save()
            sweetify.success(request, 'Muy Bien', text=' El laboratorio se ha creado exitosamente', persistent='ACEPTAR')
            return HttpResponseRedirect("/")
    context ={
        "form":LabForm(),
    }
    return render(request, 'insertar.html', context)

def update(request,laboratorio_id):
    lab = Laboratorio.objects.get(id=laboratorio_id)

    if request.method == 'POST':
        datas = request.POST.copy()
        formedition = LabForm(datas, instance=lab)
        if formedition.is_valid():
            formedition.save()
            sweetify.success(request, 'El Laboratorio se ha actualizado satisfactoriamente')
        return HttpResponseRedirect("/")
    else:

        context = {
        "formedition" : LabForm(instance=lab)
        }

        return render(request,'update.html',context)

def delete(request,laboratorio_id):
    if request.method == "POST":
        from .models import Producto, DirectorGeneral
        Producto.objects.filter(laboratorio = laboratorio_id).delete()
        DirectorGeneral.objects.filter(laboratorio = laboratorio_id).delete()

        Laboratorio.objects.get(id = laboratorio_id).delete()
        sweetify.success(request, 'El Laboratorio se ha eliminado con exito')
        return HttpResponseRedirect("/")

    context = {
        'lab': Laboratorio.objects.get(id = laboratorio_id)
    }
    return render(request, 'delete.html', context)
    
    

