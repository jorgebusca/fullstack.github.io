"""
URL configuration for webCM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("acercade/", views.acercade, name="acercade"),
    path("contacto/", views.contacto, name="contacto"),
    path("preguntas_frecuentes/", views.preguntas_frecuentes, name="preguntas_frecuentes"),
    path("usuarios", views.usuarios, name="usuarios"),
    path("lista_usuarios", views.lista_usuarios, name="lista_usuarios"),
    path("registros", views.registros, name="registros"),
    path("registros_viajes", views.registros_viajes, name="registros_viajes"),
    path("formularios", views.formularios, name="formularios"),
]
