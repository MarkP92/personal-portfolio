from django import forms
from django.core import validators

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Navn'}))
    from_email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    subject = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Emne'}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Besked'}))

    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])