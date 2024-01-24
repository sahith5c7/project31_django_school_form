from django import forms
from app.models import *
class SchoolForm(forms.Form):
    Sname=forms.CharField()
    Slocation=forms.CharField()
    Sprincipal=forms.CharField()
