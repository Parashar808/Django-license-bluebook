from django import forms
from django.forms import ModelForm
from .models import License_Fine,Bluebook_Fine

class FineForm(ModelForm):
	class Meta:
		model=License_Fine
		fields = '__all__'

class FineForm1(ModelForm):
	class Meta:
		model=Bluebook_Fine
		fields = '__all__'
