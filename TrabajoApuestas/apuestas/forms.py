from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget

class AuthenticationForm(ModelForm):
	class Meta:
		model = UserProfile
		fields = ['username', 'password']
		widgets = {
		'password': forms.PasswordInput(),
		}
		fields = '__all__'

class RegisterForm(ModelForm):
	class Meta:
		model = UserProfile
		fields = ['username', 'password1', 'password2']
		widgets = {
		'password1': forms.PasswordInput(),
		'password2': forms.PasswordInput(),
		}
		fields = '__all__'

class PartidoForm(forms.Form):
	fields = ['Local', 'Visitante', 'Inicio']

class ApuestaForm(forms.Form):
	fields = ['Resultado', 'Cantidad']
