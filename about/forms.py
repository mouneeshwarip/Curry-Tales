from django import forms
from .models import About

# Defining AboutFrom structure to display in view
class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ('title', 'content')