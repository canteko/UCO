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
from django.views.generic import DetailView
import operator
#Partidos

def verPartidosPoliticos(request):
	partidos_politicos = PartidoPolitico.objects.all()
	context = {'partidos_politicos':partidos_politicos}
	return render(request, 'verPartidosPoliticos.html', context)

def detallePartidoPolitico(request, partido_id):
	partido_politico = PartidoPolitico.objects.get(pk=partido_id)
	Votos = Voto.objects.all()
	votos_partido = 0
	if Votos:
		for x in Votos:
			if x.nombre_partido_voto.nombre_partido == partido_politico.nombre_partido:
				votos_partido = votos_partido + 1
	context = {'partido_politico':partido_politico, 'votos_partido':votos_partido}
	return render(request, 'detallePartidoPolitico.html', context)

def addPartidoPolitico(request):
	if request.method == 'POST' :
		partido_politico = PartidoPolitico()
		formulario = PartidoPoliticoForm (request.POST, instance = partido_politico)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else :
		formulario = PartidoPoliticoForm()
	return render_to_response ('addPartidoPolitico.html', {'formulario':formulario}, context_instance = RequestContext(request))

#Votos

def addVoto(request):
	if request.method == 'POST' :
		voto = Voto()
		found = 0
		formulario = VotoForm (request.POST, instance = voto)
		if formulario.is_valid():
			formulario.save()
			for i in Resultado.objects.all():
				if i.mesa_resultado.nombre_mesa == voto.mesa_voto.nombre_mesa and found == 0:
					i.votos_resultado.add(voto)
					found == 1
			return HttpResponseRedirect('/')
	else :
		formulario = VotoForm()
	return render_to_response ('addVoto.html', {'formulario':formulario}, context_instance = RequestContext(request))

#Circunscripciones

# def verCircunscripciones(request):
# 	circunscripciones = Circunscripcion.objects.all()
# 	context = {'circunscripciones':circunscripciones}
# 	return render(request, 'verCircunscripciones.html', context)

def detalleCircunscripcion(request, circunscripcion_id):
	c = Circunscripcion.objects.get(pk=circunscripcion_id)
	Mesas = MesaElectoral.objects.all()
	m_c = []
	if Mesas:
		for x in Mesas:
			if x.circunscripcion_mesa.nombre_c == c.nombre_c:
				m_c.append(x)
	context = {'circ':c, 'mesas':m_c}
	return render(request, 'detalleCircunscripcion.html', context)

def addCircunscripcion(request):
	if request.method == 'POST' :
		circunscripcion = Circunscripcion()
		formulario = CircunscripcionForm (request.POST, instance = circunscripcion)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else :
		formulario = CircunscripcionForm()
	return render_to_response ('addCircunscripcion.html', {'formulario':formulario}, context_instance = RequestContext(request))

def editarCircunscripcion(request, circunscripcion_id):
	circunscripcion = Circunscripcion.objects.get(pk=circunscripcion_id)
	formulario = CircunscripcionForm (request.POST, instance = circunscripcion)
	if formulario.is_valid():
		formulario.save()
		return HttpResponseRedirect('/')
	else :
		formulario = CircunscripcionForm()
	return render_to_response ('editarCircunscripcion.html', {'formulario':formulario, 'nombre':circunscripcion.nombre_c}, context_instance = RequestContext(request))

def eliminarCircunscripcion(request, circunscripcion_id):
   Circunscripcion.objects.get(pk=circunscripcion_id).delete()
   return redirect('/')

#Mesas

def verMesas(request):
	mesas = MesaElectoral.objects.all()
	context = {'mesas':mesas}
	return render(request, 'verMesas.html', context)

def addMesa(request):
	if request.method == 'POST' :
		mesa = MesaElectoral()
		formulario = MesaForm (request.POST, instance = mesa)
		if formulario.is_valid():
			formulario.save()
			Resultado.objects.create(mesa_resultado=mesa)
			return HttpResponseRedirect('/')
	else :
		formulario = MesaForm()
	return render_to_response ('addCircunscripcion.html', {'formulario':formulario}, context_instance = RequestContext(request))

def editarMesa(request, mesa_id):
	mesa = MesaElectoral.objects.get(pk=mesa_id)
	formulario = MesaForm (request.POST, instance = mesa)
	if formulario.is_valid():
		formulario.save()
		return HttpResponseRedirect('/')
	else :
		formulario = MesaForm()
	return render_to_response ('editarMesa.html', {'formulario':formulario, 'nombre':mesa.nombre_mesa}, context_instance = RequestContext(request))

def detalleMesa(request, mesa_id):
	mesa = MesaElectoral.objects.get(pk=mesa_id)
	Votos = Voto.objects.all()
	votos_mesa = 0
	if Votos:
		for x in Votos:
			if x.mesa_voto.nombre_mesa == mesa.nombre_mesa:
				votos_mesa = votos_mesa + 1
	context = {'mesa':mesa, 'votos_mesa':votos_mesa}
	return render(request, 'detalleMesa.html', context)


#Resultados
def calcularCircunscripcion (c):
	votos = Voto.objects.all()
	partidos = {}
	f_n_s = ["", "", 0, c.escanos_c]
	if votos:
		for i in votos:
			if i.mesa_voto.circunscripcion_mesa.nombre_c == c.nombre_c:
				if i.nombre_partido_voto.nombre_partido not in partidos.keys():
					partidos[i.nombre_partido_voto.nombre_partido] = 1
				else:
					partidos[i.nombre_partido_voto.nombre_partido] = partidos[i.nombre_partido_voto.nombre_partido] + 1
	p_ordenados = sorted(partidos, key=partidos.get, reverse=True)
	if len(partidos) == 1:
		f_n_s[0] = p_ordenados[0]
		f_n_s[2] = 1
	if len(partidos) >= 2:
		f_n_s[0] = p_ordenados[0]
		f_n_s[1] = p_ordenados[1]
		f_n_s[2] = 2
	return f_n_s

def verResultados(request):
	resultado = Resultado.objects.all()
	num_esc = {}
	nom_cir = {}
	for i in PartidoPolitico.objects.all():
		num_esc[i.nombre_partido] = 0
	for q in Circunscripcion.objects.all():
		nom_cir[q.nombre_c] = calcularCircunscripcion (q)
	for key in nom_cir:
		if nom_cir[key][2] == 1:
			num_esc[nom_cir[key][0]] = num_esc[nom_cir[key][0]] + nom_cir[key][3]
		if nom_cir[key][2] == 2:
			num_esc[nom_cir[key][0]] = num_esc[nom_cir[key][0]] + nom_cir[key][3] - 1
			num_esc[nom_cir[key][1]] = num_esc[nom_cir[key][1]] + 1
	context = {'resultado':resultado, 'dic':num_esc}
	return render(request, 'verResultados.html', context)

def detalleResultados(request, mesa_id):
	resultado = Resultado.objects.get(pk=mesa_id)
	votos = resultado.votos_resultado.all()
	partidos_votos = {}
	if votos:
		for i in votos:
			if i.nombre_partido_voto.nombre_partido not in partidos_votos.keys():
				partidos_votos[i.nombre_partido_voto.nombre_partido] = 1
			else:
				partidos_votos[i.nombre_partido_voto.nombre_partido] = partidos_votos[i.nombre_partido_voto.nombre_partido] + 1
	context = {'mesa':resultado.mesa_resultado, 'partidos_votos':partidos_votos}
	return render(request, 'detalleResultado.html', context)

#Usuarios

def userLogin(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            user = request.POST['username']
            passwd = request.POST['password']
            access = authenticate(username=user, password=passwd)
            if access is not None:
                if access.is_active:
                    login(request, access)
                    return redirect('/')
                else:
                    return render(request, 'inactive.html')
            else:
                return render(request, 'nouser.html')
    else:
        formulario = AuthenticationForm()
    context = {'formulario': formulario}
    return render(request,'login.html', context)

def userLogout(request):
	logout(request)
	return redirect('/')

#
