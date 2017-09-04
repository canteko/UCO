from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DestinatarioForm (forms.ModelForm):
	class Meta:
		model = Destinatario
		fields = '__all__'

class DestinoForm (forms.ModelForm):
	class Meta:
		model = Destino
		fields = '__all__'

class PaqueteForm (forms.ModelForm):
	class Meta:
		model = Paquete
		fields = '__all__'

class RutaForm (forms.ModelForm):
	class Meta:
		model = Ruta
		fields = '__all__'
