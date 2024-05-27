
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from .models import *
class Form_login(forms.ModelForm):
    username=forms.CharField(label='username')
    password=forms.CharField(label='password',widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','password']
class UserCreationForms(UserCreationForm):
    username=forms.CharField(label='user name')
    password1=forms.CharField(label='password',min_length=8,widget=forms.PasswordInput())
    password2=forms.CharField(label='Password confirmation',min_length=8,widget=forms.PasswordInput())
    first_name=forms.CharField(label='first name')
    email=forms.CharField(label='email')
    last_name=forms.CharField(label='last name')
    
    class Meta:
        model=User
        fields=['username','password1','password2','first_name','last_name','email']
class Product_Form(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','price','date','about','rate','slug','img']
