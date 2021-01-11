from django import forms
from django.core.files.images import get_image_dimensions
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import *
from django.contrib.auth import authenticate, get_user_model, login, logout

from .models import *
User = get_user_model()


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'tracker',
            'fname',
            'lname',
            'gender',
            'phone',
            'avatar',
            'country',
            'province',
        ]


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm', 'placeholder': 'Username'}), label='')

    email = forms.EmailField(max_length=254, required=False,  widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm', 'placeholder': 'Email'}), label='')
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-sm', 'placeholder': 'Password'}), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-sm', 'placeholder': 'Repeat Password'}), label='')

    class Meta:
        model = User
        fields = ('username',
                  'email', 'password1', 'password2', )
