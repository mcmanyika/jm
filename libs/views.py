from __future__ import unicode_literals
from datetime import datetime
from django.utils import timezone
from django.db.models.functions import ExtractDay, ExtractMonth, ExtractYear
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import connection
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect, Http404
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from blog.models import *
from .forms import *
from .models import *


# Create your views here.
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

@login_required(login_url='/')
def dash(request):
    dictionary = t_dict.objects.all().order_by('id')
    form = UserProfileForm(request.POST or None,
                           request.FILES or None)
    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect('/libs/register-confirmation/')

    context = {
        'dictionary': dictionary,
        'form': form,
    }

    template = "libs/dash.html"

    return render(request, template, context)

@login_required(login_url='/')
def user_profile(request):
    dictionary = t_dict.objects.all().order_by('id')
    form = UserProfileForm(request.POST or None,
                           request.FILES or None)
    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect('/libs/register-confirmation/')

    context = {
        'dictionary': dictionary,
        'form': form,
    }

    template = "libs/user_profile.html"

    return render(request, template, context)

@login_required(login_url='/')
def add_profile(request):
    dictionary = t_dict.objects.all().order_by('id')
    form = AddProfileForm(request.POST or None,
                           request.FILES or None)
    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect('/libs/register-confirmation/')

    context = {
        'dictionary': dictionary,
        'form': form,
    }

    template = "libs/add_profile.html"

    return render(request, template, context)

@login_required(login_url='/')
def myProfile(request):
    dictionary = t_dict.objects.all().order_by('id')
    instance = get_object_or_404(UserProfile, tracker=request.user.id)

    form = UserProfileForm(request.POST or None,
                           request.FILES or None, instance=instance)
    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect('/libs/update-confirmation/')

    context = {
        'form': form,
        'country': instance.country,
        'dictionary': dictionary,
    }

    template = "libs/user_profile.html"

    return render(request, template, context)



def gallery(request):
    photos = Gallery.objects.all().order_by('-id')

    form = PhotoForm(request.POST or None,
                           request.FILES or None)
    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect('/libs/register-confirmation/')

    context = {
        'photos': photos,
        'form': form,
    }

    template = "libs/gallery.html"

    return render(request, template, context)


def update_confirmation(request):

    context = {

    }

    template = "libs/update_confirmation.html"

    return render(request, template, context)


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/libs/add-profile/')
    else:
        form = SignUpForm()

    context = {
        "form": form,
    }
    return render(request, 'libs/register.html', context)




def register_confirmation(request):

    context = {

    }

    template = "libs/register_confirmation.html"

    return render(request, template, context)

@login_required(login_url='/')
def add_dict(request):
    form = AddDictForm(request.POST or None,
                       request.FILES or None)
    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        messages.success(request, "Saved")

    context = {
        'form': form,
    }

    template = "libs/add_dict.html"

    return render(request, template, context)

@login_required(login_url='/')
def accts(request):

    accts = User.objects.all()
   
    context = {
        'accts' : accts,

    }

    template = "libs/members.html"

    return render(request, template, context)

@login_required(login_url='/')
def ServiceProviders(request):
    dictionary = t_dict.objects.all().order_by('id')
    form = ServiceProvidersForm(request.POST or None,
                           request.FILES or None)
    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect('/libs/register-confirmation/')

    context = {
        'dictionary': dictionary,
        'form': form,
    }

    template = "libs/service_providers.html"

    return render(request, template, context)

@login_required(login_url='/')
def dash(request):
    dictionary = t_dict.objects.all().order_by('id')


    context = {
        'dictionary': dictionary,
    }

    template = "libs/dash.html"

    return render(request, template, context)
    



def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')
