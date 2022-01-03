from django.contrib.admin.options import FORMFIELD_FOR_DBFIELD_DEFAULTS
from django.forms import widgets
from django.forms.widgets import PasswordInput

 
from . models import  Signup
from django import forms
from django.forms import fields


class SignupForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=8)
    class Meta():
        model=Signup
        fields='__all__'


class LoginForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8)
    class Meta():
        model=Signup
        fields=('Email','Password')

