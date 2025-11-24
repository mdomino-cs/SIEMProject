from django import forms
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    # You can add custom fields or styling here if needed
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    submit = forms.CharField(widget=forms.SubmitInput(attrs={'value': 'Login', 'class': 'btn btn-primary'}))