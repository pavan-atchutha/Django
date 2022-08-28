from dataclasses import field
from django import forms
from .models import Student
class studentform(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
