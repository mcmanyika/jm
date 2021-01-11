from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms

# Create your models here.


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class UserProfile(models.Model):
    tracker = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    fname = models.CharField(max_length=15, null=True, blank=True)
    lname = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=25, default='', null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    province = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=10, null=True, blank=True)
    user = models.IntegerField(default=1, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return 'UserProfile {}'.format(self.id)
