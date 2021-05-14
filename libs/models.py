from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms

# Create your models here.


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class UserProfile(models.Model):
    tracker = models.IntegerField(default='')
    profession = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=25, default='', null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=10, null=True, blank=True)
    user = models.IntegerField(default=1, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return 'UserProfile {}'.format(self.id)


class t_dict(models.Model):
    category = (
        ('Country', 'Country'),
        ('Header', 'Header'),
        ('Service Provider', 'Service Provider')
    )
    header = models.CharField(max_length=50, default='')
    category = models.CharField(choices=category, max_length=20, default='')
    order = models.CharField(max_length=20, default='1')
    status = models.CharField(max_length=20, default='')
    user = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return 't_dict {}'.format(self.id)

class Gallery(models.Model):
	title = models.CharField(max_length=50, default='')
	description = models.CharField(max_length=35, default='')
	image = models.ImageField(default='', blank=True)
    
	def __str__(self):
		return self.title

class t_service_providers(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=35, default='')
    address = models.CharField(max_length=35, default='')
    phone = models.CharField(max_length=15, default='')
    email = models.EmailField()
    contact = models.CharField(max_length=35, default='')
    website = models.CharField(max_length=35, default='')
    user = models.IntegerField(default=1, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.name