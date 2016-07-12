"""travis_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from ingreso_pacientes.views import listar_crear_paciente,detalles_paciente#, pacientes_por_diagnosticos

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pacientes/$',listar_crear_paciente),
    url(r'^pacientes/(?P<pk>[\d]+)/$',detalles_paciente),
    # url(r'^consultas/$',pacientes_por_diagnosticos)
]
