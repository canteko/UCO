from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from random import random
from datetime import datetime, date, time, timedelta

#Users

class Equipo(models.Model):
	winrate_init = models.FloatField(default=random())
	name = models.CharField(max_length=100)
	# won = models.IntegerField(default=0)
	# even = models.IntegerField(default=0)
	# lost = models.IntegerField(default=0)
	matches = models.IntegerField(default=5)

	def __str__(self):
		return self.name

class Partido(models.Model):
	local = models.ForeignKey(Equipo, related_name='%(class)s_local')
	visitante = models.ForeignKey(Equipo, related_name='%(class)s_visitante')
	puntos_local = models.IntegerField(default=0)
	puntos_visitante = models.IntegerField(default=0)
	empezado = models.BooleanField(default=False)
	terminado = models.BooleanField(default=False)
	inicio = models.DateTimeField()
	fin = models.DateTimeField()
	processed = models.BooleanField(default=False)
	ratio_local = models.FloatField(default=0)
	ratio_visitante = models.FloatField(default=0)
	ratio_even = models.FloatField(default=0)
	str_bet = models.CharField(default="0", max_length=1)

	def __str__(self):
		return self.local.name+" vs "+self.visitante.name

	def comprobar(self):
		if not(self.processed):
			if(self.inicio<=datetime.now() and self.empezado==False):
				self.empezado = True
			if(self.fin<=datetime.now() and self.terminado==False):
				self.terminado = True
			if(self.terminado == True and self.processed == False):
				for i in range(0,6):
					r1=random()
					if(r1<=self.local.winrate_init):
						self.puntos_local=self.puntos_local+1
					r2=random()
					if(r2<=self.visitante.winrate_init):
						self.puntos_visitante=self.puntos_visitante+1
				self.local.matches=self.local.matches+1
				self.visitante.matches=self.visitante.matches+1
				if(self.puntos_local>self.puntos_visitante):
					self.str_bet="1"
					self.local.winrate_init=(self.local.winrate_init*(self.local.matches-1)+1)/self.local.matches
					self.visitante.winrate_init=(self.visitante.winrate_init*(self.local.matches-1))/self.visitante.matches
				elif(self.puntos_local<self.puntos_visitante):
					self.str_bet="2"
					self.local.winrate_init=(self.local.winrate_init*(self.local.matches-1))/self.local.matches
					self.visitante.winrate_init=(self.visitante.winrate_init*(self.local.matches-1)+1)/self.visitante.matches
				else:
					self.str_bet="x"
					self.local.winrate_init=(self.local.winrate_init*(self.local.matches-1)+0.5)/self.local.matches
					self.visitante.winrate_init=(self.visitante.winrate_init*(self.local.matches-1)+0.5)/self.visitante.matches
				self.processed = True
				self.save()

#Apuestas

class Apuesta(models.Model):
	partido_id = models.IntegerField()
	credit_amount = models.IntegerField()
	ratio = models.FloatField()
	choice_bet = models.CharField(max_length=1)
	match_finished = models.BooleanField(default=False)
	claimed = models.BooleanField(default=False)
	won = models.BooleanField(default=False)

	def __str__(self):
		return str(self.partido_id) + "_" + str(self.credit_amount) + "_" + str(self.ratio) + "_" + self.choice_bet

	def comprobar(self):
		p=Partido.objects.get(id=self.partido_id)
		if(self.match_finished == False):
			self.match_finished = p.terminado
		if(self.match_finished == True):
			if(self.choice_bet==p.str_bet):
				self.won=True
		self.save()

	def claim(self, id_profile):
		print("Hi")
		user=UserProfile.objects.get(id=id_profile)
		if(not self.claimed and self.won):
			print(user.credit)
			user.credit = user.credit + int(self.ratio*self.credit_amount)
			print(user.credit)
		self.claimed=True
		user.save()
		self.save()

# Usuarios

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	credit = models.IntegerField(default=0)
	bets = models.ManyToManyField(Apuesta)

	def __str__(self):
		return self.user.username
