from django.shortcuts import render
from .import views

def v_index(request):

    context = {

    }
    return render ( request, 'v_index.html', context )


