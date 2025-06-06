from django import forms
from .models import Job, Application

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'description', 'location']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'required': True}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'email', 'phone', 'dob', 'education', 'experience', 'resume']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }