from django import forms
import datetime

from django.forms.formsets import formset_factory
from demo.models.personne import Personne
from django.forms import formset_factory

class FormPers(forms.Form):
    nom=forms.CharField(max_length=40)
    date_from=forms.DateField(widget=forms.DateInput
    (attrs={'type': 'date'}
   
    ))

class FormPersonne(forms.ModelForm):
    class Meta:
        model=Personne
        fields=['nom','prenom','adresse','ville']

class FrmPers(forms.ModelForm):
    class Meta:
        model=Personne
        fields=['nom','prenom','adresse','ville']


PersonneFormset = formset_factory(
    Personne)
