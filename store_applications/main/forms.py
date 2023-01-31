from django.forms import ModelForm
from django import forms
from .models import Application, Position, Applicant, Test
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

'''class ApplicationSubmission(ModelForm):
    applicant = forms.ModelChoiceField(queryset=Applicant.objects.all(), label="First Name")
    #applicant = forms.CharField(label="First Name", max_length=255)
    last_name = forms.CharField(label="Last Name",max_length=255)
    resume = forms.FileField(label="Resume")
    cover_letter = forms.FileField(label="Cover Letter")
    date_submitted = forms.DateField(label="Subission Date")
    position = forms.ModelChoiceField(queryset=Position.objects.all(), label="Position")
    # manager =  forms.ModelChoiceField(queryset=Manager.objects.all(), label="Manager")
    class Meta:
        model = Application
        fields = "__all__"
'''

class ApplicationSubmission(ModelForm):
    class Meta:
        model = Application
        fields = ['applicant', 'resume', 'cover_letter', 'date_submitted', 'position']
        labels = {
            'applicant': 'Applicant Name',
            'resume': 'Resume',
            'cover_letter': 'Cover Letter',
            'date_submitted': 'Date of Submission',
            'position': 'Choose a position to apply for',
        }
        help_texts = {
            'resume': '(Please use .pdf, .jpeg, or .png only!)',
            'cover_letter': '(Please use .pdf, .jpeg, or .png only!)',
        }
        widgets = {
            #'applicant': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'applicant'}),
            #'resume': forms.FileField(attrs={'class': 'form-control'}), 
            #'cover_letter': forms.FileField(attrs={'class': 'form-control'}), 
            'date_submitted': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}), 
            #'position': forms.TextInput(attrs={'class': 'form-control'}), 
        }


class ApplicantSignUp(ModelForm):
    
    class Meta:
        model = Applicant
        fields = ['user', 'first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'address']
        labels = {
            'user': 'Username',
        }
        help_texts = {
            'phone_number': '(Please use numbers only!)'
        }

        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First'}), 
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}), 
            'date_of_birth': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}), 
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'myemail@email.com'}), 
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '7774445555'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '10 Tech Store St. Las Vegas, NV, 89018'}),
        }

class Test(ModelForm):
    class Meta:
        model = Test
        fields = ['resume', 'applicant', 'position']