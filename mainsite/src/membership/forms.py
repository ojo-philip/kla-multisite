from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):
    date_of_birth = forms.CharField(max_length=250, required=True, widget=forms.TextInput(attrs={
            'placeholder':"e.g 2022-05-24",

    }))

    class Meta:
        model = Application
        fields = ['email','surname','other_names', 'country', 'course_of_study', 'level_of_study', 'marital_status', 'your_whatsapp_number', 'date_of_birth', 'be_a_member','organization_meeting', 'potential_executive', 'skill', 'leadership', 'your_hobbies', 'unit']