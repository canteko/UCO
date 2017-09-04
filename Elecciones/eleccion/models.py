from django.db import models
from django.utils.encoding import smart_text as smart_unicode

class PartidoPolitico(models.Model):
	nombre_partido = models.CharField(max_length=100)
	pos_eje_partido = models.CharField(max_length=50)
	descripcion_partido = models.TextField()

	def __str__(self):
		return self.nombre_partido

class Circunscripcion(models.Model):
	nombre_c = models.CharField(max_length=100)
	escanos_c = models.IntegerField()

	def __str__(self):
		return self.nombre_c

class MesaElectoral(models.Model):
	nombre_mesa = models.CharField(max_length=100)
	circunscripcion_mesa = models.ForeignKey(Circunscripcion)

	def __str__(self):
		return self.nombre_mesa

class Voto(models.Model):
	nombre_partido_voto = models.ForeignKey(PartidoPolitico)
	mesa_voto = models.ForeignKey(MesaElectoral)

	def __str__(self):
		return (self.nombre_partido_voto.nombre_partido)

class Resultado(models.Model):
	mesa_resultado = models.ForeignKey(MesaElectoral)
	votos_resultado = models.ManyToManyField(Voto)

	def __str__(self):
		return (self.mesa_resultado.nombre_mesa)

# Create your models here.
