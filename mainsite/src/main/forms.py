from django import forms
from .models import Contact



class ContactForm(forms.ModelForm):
  name = forms.CharField(label='', max_length=250, required=True, widget=forms.TextInput(attrs={
        'placeholder':"Name",
        "class": "form-item"

    }))
  subject = forms.CharField(label='', max_length=250, required=False, widget=forms.TextInput(attrs={
        'placeholder':"Subject",
        "class": "form-item"

    }))
  email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'placeholder':"Email Address",
        "class": "form-item"
    }))
  message = forms.CharField(label='', widget=forms.Textarea(attrs={
        'placeholder': "Write your message here",
        'rows': 3,
        "class": "form-item"

    }))

  class Meta:
    model = Contact
    fields = ["name", "email", "subject", "message"]