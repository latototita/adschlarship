from django.forms import ModelForm
from django import forms
from .models import *

class Formone(forms.ModelForm):
	class Meta:
		model=Form1
		fields=('name','email','age',)
class Formstwo(forms.ModelForm):
	class Meta:
		model=Form1
		fields=('date_of_birth','nationality',)

class Formthree(forms.ModelForm):
	class Meta:
		model=Form2
		fields=('Cv','last_level_of_studying',)
class Formfour(forms.ModelForm):
	class Meta:
		model=Form2
		fields=('letter_to_employer',)