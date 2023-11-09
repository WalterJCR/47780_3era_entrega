from django.shortcuts import render

# Create your views here.
from Automovil.models import Auto, Alquiler, Conductor

# Create your views here.
def listar_Auto(request):
    contexto = {
        'Autos' : Auto.objects.all()
    }
    http_response = render(
        request=request,
        template_name='Automovil/autos.html',
        context=contexto,
    )
    return http_response

def listar_Alquiler(request):
    contexto = {
        'Autos' : Alquiler.objects.all()
    }
    http_response = render(
        request=request,
        template_name='Automovil/autos.html',
        context=contexto,
    )
    return http_response

def listar_Conductor(request):
    contexto = {
        'Autos' : Conductor.objects.all()
    }
    http_response = render(
        request=request,
        template_name='Automovil/autos.html',
        context=contexto,
    )
    return http_response