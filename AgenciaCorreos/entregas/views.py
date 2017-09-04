from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.conf import settings
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import View
from django.views.generic import TemplateView

#Destinatario

def verDestinatario(request):
	destinatarios = Destinatario.objects.all()
	context = {'destinatarios':destinatarios}
	return render(request, 'verDestinatario.html', context)

def detalleDestinatario(request, destinatario_id):
	destinatario = Destinatario.objects.get(pk=destinatario_id)
	context = {'destinatarioDetalle':destinatario}
	return render(request, 'detalleDestinatario.html', context)

def addDestinatario(request):
	if request.method == 'POST' :
		destinatario = Destinatario()
		formulario = DestinatarioForm (request.POST, instance = destinatario)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else :
		formulario = DestinatarioForm()
	return render_to_response ('addDestinatario.html', {'formulario':formulario}, context_instance = RequestContext(request))

#Destino

def verDestino(request):
	destinos = Destino.objects.all()
	context = {'destinos':destinos}
	return render(request, 'verDestino.html', context)

def detalleDestino(request, destino_id):
	destino = Destino.objects.get(pk=destino_id)
	context = {'destinoDetalle':destino}
	return render(request, 'detalleDestino.html', context)

def addDestino(request):
	if request.method == 'POST' :
		destino = Destino()
		formulario = DestinoForm (request.POST, instance = destino)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else :
		formulario = DestinoForm()
	return render_to_response ('addDestino.html', {'formulario':formulario}, context_instance = RequestContext(request))

#Paquete

def verPaquete(request):
	paquetes = Paquete.objects.all()
	context = {'paquetes':paquetes}
	return render(request, 'verPaquete.html', context)

def detallePaquete(request, paquete_id):
	paquete = Paquete.objects.get(pk=paquete_id)
	context = {'paqueteDetalle':paquete}
	return render(request, 'detallePaquete.html', context)

def addPaquete(request):
	if request.method == 'POST' :
		paquete = Paquete()
		formulario = PaqueteForm (request.POST, instance = paquete)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else :
		formulario = PaqueteForm()
	return render_to_response ('addPaquete.html', {'formulario':formulario}, context_instance = RequestContext(request))

#Rutas

class verRuta(View):
    template_name = 'verRuta.html'
    def get(self, request, *args, **kwargs):
        rutas = Ruta.objects.all()
        return render(request, self.template_name, {'rutas':rutas})


class addRuta(View):
    form_class = RutaForm
    template_name = 'addRuta.html'

    def get(self, request, *args, **kwargs):
        formulario = self.form_class()
        return render(request, self.template_name, {'formulario': formulario})

    def post(self, request, *args, **kwargs):
        formulario = self.form_class(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'formulario': formulario})


class detalleRuta(View):
    template_name = 'detalleRuta.html'

    def get(self, request, *arg, **kwargs):
        id = self.kwargs['Ruta_id']
        ruta = get_object_or_404(Ruta, pk = id)
        return render(request,self.template_name,{'rutaDetalle':ruta,'user':request.user})
