from django.contrib import admin
from django.conf.urls import include, url
from libs.views import *

urlpatterns = [

    url(r'^', dashboard, name='profile'),



]
