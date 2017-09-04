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
from datetime import datetime, date, time, timedelta

#Auxiliares

def dateTimeValidation(date):
	try:
		dat = datetime(int(date[6:10]), int(date[3:5]), int(date[0:2]), int(date[11:13]), int(date[14:16]))
	except ValueError:
		return False
	return True

def createRatio(t1, t2):
	wr1=t1.winrate_init
	wr2=t2.winrate_init
	wrline=wr1/wr2
	even_ratio=(1+abs(1-wrline))-0.3*(abs(1-wrline))
	ratio_1=(1+(wr2/wr1))-0.3*(wr2/wr1)
	ratio_2=(1+(wr1/wr2))-0.3*(wr1/wr2)
	return ratio_1, ratio_2, even_ratio
#Index

def index(request):
	context={}
	if request.user.is_authenticated() and not (request.user.id in UserProfile.objects.values_list('user', flat=True)):
		# print(UserProfile.objects.values_list('user', flat=True))
		# print(request.user.id)
		UserProfile.objects.create(user=request.user, credit=0)
	if request.user.is_authenticated():
		print("Hola")
		user_profile = UserProfile.objects.get(user=request.user)
		context = {'user_profile':user_profile}
	return render(request,'index.html', context)

#Usuarios

def profile(request):
	context={}
	if request.user.is_authenticated():
		user_profile = UserProfile.objects.get(user=request.user)
		bets = user_profile.bets.all()
		for i in bets:
			i.comprobar()
			i.claim(user_profile.id)
		context = {'user_profile':user_profile, 'bets':bets}
	return render(request,'profile.html', context)

def userRegister(request):
	fallo=''
	if request.method == 'POST':
		formulario = RegisterForm(request.POST)
		if formulario.is_valid:
			user = request.POST['username']
			passwd1 = request.POST['password1']
			passwd2 = request.POST['password2']
			print(User.objects.values_list('username', flat=True), user)
			if user in User.objects.values_list('username', flat=True):
				fallo = '*Ese usuario ya existe'
			elif passwd1 != passwd2:
				fallo = '*Las contraseñas no son iguales'
			else:
				registeredUser = User.objects.create_user(username=user, password=passwd1)
				UserProfile.objects.create(user=registeredUser)
				access = authenticate(username=user, password=passwd1)
				if access is not None:
					login(request, access)
					return redirect('/')
	else:
		formulario = RegisterForm()
	context = {'formulario': formulario, 'fallo':fallo}
	return render(request,'register.html', context)

def userLogin(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            user = request.POST['username']
            passwd = request.POST['password']
            access = authenticate(username=user, password=passwd)
            if access is not None:
                login(request, access)
                return redirect('/')
            else:
                return render(request, 'nouser.html')
    else:
        formulario = AuthenticationForm()
    context = {'formulario': formulario}
    return render(request,'login.html', context)

def userLogout(request):
	logout(request)
	return redirect('/')

#Partidos

def addPartido(request):
	fallo=''
	equipos=Equipo.objects.all()
	if request.method == 'POST':
		formulario = PartidoForm(request.POST)
		if formulario.is_valid():
			local = request.POST['Local']
			visitor = request.POST['Visitante']
			date = request.POST['Inicio']
			if(local==visitor):
				fallo="No puedes enfrentar a un equipo con sí mismo"
			elif not(dateTimeValidation(date)):
				fallo="El formato de fecha no es correcto"
			elif not(datetime(int(date[6:10]), int(date[3:5]), int(date[0:2]), int(date[11:13]), int(date[14:16]))>=datetime.now()):
				fallo="La fecha ya ha pasado"
			else:
				d=datetime(int(date[6:10]), int(date[3:5]), int(date[0:2]), int(date[11:13]), int(date[14:16]))
				r1, r2, re = createRatio(Equipo.objects.get(id=local), Equipo.objects.get(id=visitor))
				Partido.objects.create(local=Equipo.objects.get(id=local), visitante=Equipo.objects.get(id=visitor), inicio=d, fin=d+timedelta(minutes=1), ratio_local=r1, ratio_visitante=r2, ratio_even=re)
				return redirect('/')
	else:
		formulario = PartidoForm()

	context = {'formulario': formulario, 'fallo':fallo, 'equipos':equipos}
	return render(request,'addPartido.html', context)

def verPartidos(request):
	partidos = Partido.objects.all()
	for i in partidos:
		i.comprobar()
	context = {'partidos':partidos}
	return render(request, 'verPartidos.html', context)

def addApuesta(request, partido_id):
	fallo=""
	ratio=0.0
	partido=Partido.objects.get(pk=partido_id)
	if not request.user.is_authenticated():
		return redirect('/login')
	user_profile = UserProfile.objects.get(user=request.user)
	if request.method == 'POST':
		formulario = ApuestaForm(request.POST)
		if formulario.is_valid:
			choice_bet = request.POST['Resultado']
			credits = int(request.POST['Creditos'])
			if credits > user_profile.credit:
				fallo="No tienes tantos creditos"
			else:
				if(choice_bet=="1"):
					ratio=partido.ratio_local
				elif(choice_bet=="2"):
					ratio=partido.ratio_visitante
				else:
					ratio=partido.ratio_even
				bet=Apuesta.objects.create(partido_id=partido_id, credit_amount=credits, ratio=ratio, choice_bet=choice_bet)
				user_profile.credit=user_profile.credit-credits
				user_profile.bets.add(bet)
				user_profile.save()
	else:
		formulario = ApuestaForm()
	context = {'formulario': formulario, 'partido':partido, 'user_profile':user_profile, 'fallo':fallo}
	return render(request,'apostar.html', context)

# def detallePartidoPolitico(request, partido_id):
# 	partido_politico = PartidoPolitico.objects.get(pk=partido_id)
# 	Votos = Voto.objects.all()
# 	votos_partido = 0
# 	if Votos:
# 		for x in Votos:
# 			if x.nombre_partido_voto.nombre_partido == partido_politico.nombre_partido:
# 				votos_partido = votos_partido + 1
# 	context = {'partido_politico':partido_politico, 'votos_partido':votos_partido}
# 	return render(request, 'detallePartidoPolitico.html', context)
