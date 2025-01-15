from django import forms
from .models import About, Contact

# Defining AboutFrom structure to display in view
class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ('title', 'content')

# Defining ContactFrom structure to display in view
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'email': 'Email address',
            'message': 'Write a message to us...',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
