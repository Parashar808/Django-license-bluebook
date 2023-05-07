from django import forms
from django.forms import ModelForm
from .models import License_Fine,Bluebook_Fine,license,bluebook

class FineForm(ModelForm):
	class Meta:
		model=License_Fine
		fields = '__all__'

class FineForm1(ModelForm):
	class Meta:
		model=Bluebook_Fine
		fields = '__all__'

class LicenseForm(ModelForm):
	class Meta:
		model=license
		fields='__all__'


class BluebookForm(ModelForm):
	class Meta:
		model=bluebook
		fields='__all__'