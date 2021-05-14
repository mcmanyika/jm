from django import forms
from django.core.files.images import get_image_dimensions
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import *
from django.contrib.auth import authenticate, get_user_model, login, logout

from .models import *
User = get_user_model()


class UserProfileForm(forms.ModelForm):
    profession = forms.CharField(max_length=30, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm', 'placeholder': 'Profession'}), label='')
    gender = forms.CharField(max_length=30, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm', 'placeholder': 'Gender'}), label='')
    phone = forms.CharField(max_length=30, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm', 'placeholder': 'Phone'}), label='')
    country = forms.CharField(max_length=30, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm', 'placeholder': 'Country'}), label='')

    class Meta:
        model = UserProfile
        fields = [
            'tracker',
            'profession',
            'gender',
            'phone',
            'country',
        ]

class AddProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'tracker',
        ]

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=False, widget = forms.TextInput(attrs={'class' : 'form-control form-control-sm','placeholder':'Username'}), label='')
    
    first_name = forms.CharField(max_length=30, required=False, widget = forms.TextInput(attrs={'class' : 'form-control form-control-sm','placeholder':'First Name'}), label='')
    last_name = forms.CharField(max_length=30, required=False, widget = forms.TextInput(attrs={'class' : 'form-control form-control-sm','placeholder':'Last Name'}), label='')
    
    email = forms.EmailField(max_length=254, required=False,  widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm', 'placeholder': 'Email'}), label='')
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-sm', 'placeholder': 'Password'}), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-sm', 'placeholder': 'Repeat Password'}), label='')

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name',
                  'email', 'password1', 'password2', )


class AddDictForm(forms.ModelForm):
    header = forms.CharField(max_length=30, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm', 'placeholder': 'Header'}), label='')
    
    class Meta:
        model = t_dict
        fields = [
            'header',
            'category',
            'status',
            'user',
        ]

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title',
                  'description',
                  'image',
                  ]  


class ServiceProvidersForm(forms.ModelForm):
    name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(
    attrs={'class': 'form-control form-control-sm', 'placeholder': 'Company Name'}), label='')
    description = forms.CharField(max_length=30, required=False, widget=forms.TextInput(
    attrs={'class': 'form-control form-control-sm', 'placeholder': 'Type of Service'}), label='')
    address = forms.CharField(max_length=30, required=False, widget=forms.TextInput(
    attrs={'class': 'form-control form-control-sm', 'placeholder': 'Address'}), label='')
    phone = forms.CharField(max_length=30, required=False, widget=forms.TextInput(
    attrs={'class': 'form-control form-control-sm', 'placeholder': 'Phone'}), label='')
    email = forms.CharField(max_length=30, required=False, widget=forms.TextInput(
    attrs={'class': 'form-control form-control-sm', 'placeholder': 'Email'}), label='')
    website = forms.CharField(max_length=30, required=False, widget=forms.TextInput(
    attrs={'class': 'form-control form-control-sm', 'placeholder': 'Website'}), label='')
    contact = forms.CharField(max_length=30, required=False, widget=forms.TextInput(
    attrs={'class': 'form-control form-control-sm', 'placeholder': 'Contact Person'}), label='')
    class Meta:
        model = t_service_providers
        fields = [
            'name',
            'description',
            'address',
            'phone',
            'email',
            'website',
            'contact',
            'user',
        ]
