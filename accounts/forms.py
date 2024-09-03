from django import forms
from django.contrib.auth.forms import AuthenticationForm

class EmailLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'autofocus': True}))




class LoginForm(forms.Form):
    email = forms.CharField(max_length=63, widget=forms.EmailInput(attrs={'class':'mx-auto w-full border border-gray-300 focus:outline-none focus:outline-gray-400 rounded-md'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class':'mx-auto w-full border border-gray-300 focus:outline-none focus:outline-gray-400 rounded-md'}))