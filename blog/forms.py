from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    name=forms.CharField(max_length=100,required=True)
    email=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea)
    
    def clean_name(self):
        name=self.cleaned_data.get('name')
        if name=='shabeeth':
            raise ValidationError('Name cannot be shabeeth')
        return name
    def clean_email(self):
        email=self.cleaned_data.get('email')
        