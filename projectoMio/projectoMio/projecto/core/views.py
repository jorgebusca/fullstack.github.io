from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, "core/index.html")

def acercade(request):
    return render(request, "core/acercaDe.html")

def portfolio(request):
    return render(request, "core/portfolio.html")

def contacto(request):
    return render(request, "core/contacto.html")

def formulario(request):
    return render(request, "core/formulario.html")

def preguntas_frecuentes(request):
    return render(request, "core/preguntas_frecuentes.html")

def usuarios(request):
    return render(request, "core/usuarios.html")

def lista_usuarios(request):
    return render(request, "core/lista_usuarios.html")

def registro(request):
    return render(request, "core/registro.html")

def registro_viajes(request):
    return render(request, "core/registro_viajes.html")