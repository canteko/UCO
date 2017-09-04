from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView, ListView
from apuestas import views
from .views import *

urlpatterns = [
	url(r'^addPartido', views.addPartido, name = "Crear Partido"),
	url(r'^verPartidos', views.verPartidos, name = "Partidos"),
	url(r'^apostar/(?P<partido_id>\d+)', views.addApuesta, name = "Apostar"),
]
