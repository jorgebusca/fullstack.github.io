from django.shortcuts import render, HttpResponse

html_base = """
<h1>web mio</h1>
    <ul>
        <li><a href="">Inicio</a></li>
        <li><a href="/acercade">A Cerca de</a></li>
        <li><a href="/contacto">Contacto</a></li>
        <li><a href="/preguntas_frecuentes">Preguntas Frecuentes</a></li>
        <li><a href="/usuarios">Usuarios</a></li>
        <li><a href="/lista_usuarios">Lista de Usuarios</a></li>
        <li><a href="/registros">Registros</a></li>
        <li><a href="/registros_viajes">Registros Viajes</a></li>
        <li><a href="/formularios">Formularios</a></li>
    </ul>    

"""

# Create your views here.


def home(request):
    return HttpResponse(html_base + """<h2>Home</h2>""")

def acercade(request):
    return HttpResponse(html_base + """<h2>acercade</h2>""")

def contacto(request):
    return HttpResponse(html_base + """<h2>contacto</h2>""")

def preguntas_frecuentes(request):
    return HttpResponse(html_base + """<h2>preguntas_frecuentes</h2>""")

def usuarios(request):
    return HttpResponse(html_base + """<h2>usuarios</h2>""")

def lista_usuarios(request):
    return HttpResponse(html_base + """<h2>lista_usuarios</h2>""")

def registros(request):
    return HttpResponse(html_base + """<h2>registros</h2>""")

def registros_viajes(request):
    return HttpResponse(html_base + """<h2>registros_viajes</h2>""")

def formularios(request):
    return HttpResponse(html_base + """<h2>formularios</h2>""")