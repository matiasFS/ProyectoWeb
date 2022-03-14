from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', required=True)
    lastName = forms.CharField(label='Last Name', required=True)
    email = forms.CharField(label='Email', required=True)
    content = forms.CharField(label='Content', widget=forms.Textarea)