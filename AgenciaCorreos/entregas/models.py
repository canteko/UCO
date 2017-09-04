from django.db import models
from django.utils.encoding import smart_text as smart_unicode
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils import timezone


class Destinatario(models.Model):
    nombre=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)

    def __str__(self):

        return self.nombre


class Destino(models.Model):
	destinatario=models.ForeignKey(Destinatario)
	descripcion=models.TextField()
	distancia=models.IntegerField()

	def __str__(self):

		return self.destinatario.direccion

class Paquete(models.Model):
	contenido=models.CharField(max_length=100)
	valor=models.IntegerField()
	destinatario=models.ForeignKey(Destinatario)

	def __str__(self):

		return self.contenido
# class Viaje(models.Model):
#
#     destino=models.ForeignKey(Destino)
#     coste=models.IntegerField()
#     numero_de_dias=models.IntegerField()
#     modo_desplazamiento=models.CharField(max_length=100)
#
#     def __unicode__(self):
#
#         return (self.detino.lugar)

class Ruta(models.Model):
	Nombre_Ruta=models.CharField(max_length=100)
	destinos=models.ManyToManyField(Destino)
	# Precio_total=models.IntegerField()
	# Duracion_Total=models.IntegerField()

	def __str__(self):

		return (self.Nombre_Ruta)
