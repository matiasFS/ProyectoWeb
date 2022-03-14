from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', required=True)
    surname = forms.CharField(label='Surname', required=True)
    email = forms.CharField(label='Email', required=True)
    content = forms.CharField(label='Content')