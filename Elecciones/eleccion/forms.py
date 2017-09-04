from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PartidoPoliticoForm (forms.ModelForm):
	class Meta:
		model = PartidoPolitico
		fields = '__all__'

class VotoForm (forms.ModelForm):
	class Meta:
		model = Voto
		fields = '__all__'

class CircunscripcionForm (forms.ModelForm):
	class Meta:
		model = Circunscripcion
		fields = '__all__'

class MesaForm (forms.ModelForm):
	class Meta:
		model = MesaElectoral
		fields = '__all__'

class AuthenticationForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']
		widgets = {
		'password': forms.PasswordInput(),
		}
		fields = '__all__'
