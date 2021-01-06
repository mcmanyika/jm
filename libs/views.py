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


# Create your views here.

def dashboard(request):

    context = {

    }

    template = "libs/dashboard.html"

    return render(request, template, context)
