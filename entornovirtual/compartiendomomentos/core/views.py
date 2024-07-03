from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, "core/home.html")

def acercade(request):
    return render(request, "core/acercade.html")

def contacto(request):
    return render(request, "core/contacto.html")

def lista_usuario(request):
    return render(request, "core/lista_usuario.html")

def preguntas_frecuentes(request):
    return render(request, "core/preguntas_frecuentes.html")

def registro(request):
    return render(request, "core/registro.html")

def registroviaje(request):
    return render(request, "core/registroviaje.html")

def usuario(request):
    return render(request, "core/usuario.html")

def formulario(request):
    return render(request, "core/formulario.html")
