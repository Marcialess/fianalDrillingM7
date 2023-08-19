from django import forms
from .models import Laboratorio

class LabForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        exclude = []
