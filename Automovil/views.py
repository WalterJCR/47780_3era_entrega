from django.shortcuts import render

from django.urls import reverse
from django.db.models import Q

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

def crear_Automovil(request):
    if request.method == "POST":
        # Guardado de datos
        # Creo un objeto formulario con la data que envio el usuario
        formulario = AutoForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            marca = data["marca"]
            modelo = data["modelo"]
            color = data["color"]
            placa = data["placa"]
            año = data["año"]
            precio = data["precio"]
            # creo un auto en memoria RAM
            Auto = Auto(marca=marca, modelo=modelo, color=color, placa=placa, año=año, precio=precio)
            # Lo guardan en la Base de datos
            Auto.save()

            # Redirecciono al usuario a la lista de autos
            url_exitosa = reverse('lista_autos') 
            return redirect(url_exitosa)
    else:  # GET
        # Descargar formulario inicial
        formulario = AutoForm()
    http_response = render(
        request=request,
        template_name='formulario_auto.html',
        context={'formulario': formulario}
    )
    return http_response


def buscar_auto(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        Auto = Auto.objects.filter(
            Q(nombre_icontains=busqueda) | Q(marcacontains=busqueda) | Q(marcacontains=busqueda) | Q(genero_contains=busqueda)
        )

        contexto = {
            "Autos": Auto,
        }
        http_response = render(
            request=request,
            template_name='lista_auto.html',
            context=contexto,
        )
        return http_response

from django.shortcuts import render, redirect
from .models import Auto, Conductor, Alquiler
from .forms import AutoForm, ConductorForm, AlquilerForm

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from Automovil.models import Auto, Conductor, Alquiler
from Automovil.forms import AutoFormForm, ConductorForm, AlquilerFormForm

class AutoListView(ListView):
    model = Auto
    template_name = 'auto.html'
    context_object_name = 'autos'
    paginate_by = 10

class AutoDetailView(DetailView):
    model = Auto
    template_name = 'auto.html'
    context_object_name = 'auto'

class AutoCreateView(CreateView):
    model = Auto
    template_name = 'auto.html'
    fields = ['marca', 'modelo', 'color', 'placa', 'precio']

class AutoUpdateView(UpdateView):
    model = Auto
    template_name = 'auto.html'
    fields = ['marca', 'modelo', 'color', 'placa', 'precio']

class AutoDeleteView(DeleteView):
    model = Auto
    template_name = 'auto.html'
    success_url = '/autos/'

class ConductorListView(ListView):
    model = Conductor
    template_name = 'auto.html'
    context_object_name = 'autos'
    paginate_by = 10

class ConductorDetailView(DetailView):
    model = Conductor
    template_name = 'auto.html'
    context_object_name = 'auto'

class ConductorCreateView(CreateView):
    model = Conductor
    template_name = 'auto.html'
    fields = ['nombre', 'dni', 'licencia', 'telefono', 'email']

class ConductorUpdateView(UpdateView):
    model = Conductor
    template_name = 'auto.html'
    fields = ['nombre', 'dni', 'licencia', 'telefono', 'email']

class ConductorDeleteView(DeleteView):
    model = Conductor
    template_name = 'auto.html'
    success_url = '/Conductor/'

class AlquilerListView(ListView):
    model = Alquiler
    template_name = 'auto.html'
    context_object_name = 'Alquiler'
    paginate_by = 10

class AlquilerDetailView(DetailView):
    model = Alquiler
    template_name = 'auto.html'
    context_object_name = 'Alquiler'

class AlquilerCreateView(CreateView):
    model = Conductor
    template_name = 'auto.html'
    fields = ['auto', 'conductor', 'fecha_inicio', 'fecha_fin', 'costo']

class AlquilerUpdateView(UpdateView):
    model = Alquiler
    template_name = 'auto.html'
    fields = ['marca', 'modelo', 'color', 'placa', 'precio']

class AlquilerDeleteView(DeleteView):
    model = Alquiler
    template_name = 'auto.html'
    success_url = '/Alquiler/'