from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView, ListView
from eleccion import views
from .views import *

urlpatterns = [
	url(r'^verCircunscripciones/$', ListView.as_view(model=Circunscripcion, template_name="verCircunscripciones.html")),
	url(r'^verPartidosPoliticos', views.verPartidosPoliticos, name = "Ver Partidos Politicos"),
	url(r'^detallePartidoPolitico/(?P<partido_id>\d+)', views.detallePartidoPolitico, name='Detalles Partido Politico'),
	url(r'^addPartidoPolitico', views.addPartidoPolitico, name = "Añadir Partido Politico"),
	url(r'^detalleCircunscripcion/(?P<circunscripcion_id>\d+)', views.detalleCircunscripcion, name='Detalles Circunscripcion'),
	url(r'^editarCircunscripcion/(?P<circunscripcion_id>\d+)', views.editarCircunscripcion, name='Editar Circunscripcion'),
	url(r'^eliminarCircunscripcion/(?P<circunscripcion_id>\d+)', views.eliminarCircunscripcion, name='Eliminar Circunscripcion'),
	url(r'^addCircunscripcion', views.addCircunscripcion, name = "Añadir Circunscripcion"),
	url(r'^verMesas', views.verMesas, name = "Ver Mesas"),
	url(r'^editarMesa/(?P<mesa_id>\d+)', views.editarMesa, name='Editar Mesa'),
	url(r'^verResultados', views.verResultados, name = "Ver Resultados"),
	url(r'^detalleMesa/(?P<mesa_id>\d+)', views.detalleMesa, name='Detalles Mesa'),
	url(r'^detalleResultados/(?P<mesa_id>\d+)', views.detalleResultados, name='Detalles Resultados'),
	url(r'^addMesa', views.addMesa, name = "Añadir Mesa"),
	url(r'^addVoto', views.addVoto, name = "Votar"),
]
