from django.contrib import admin
from django.conf.urls import include, url
from libs.views import *

urlpatterns = [
    url(r'^logout/$', Logout, name='logout'),
    url(r'^register-member/$', register, name='register-member'),
    url(r'^user-profile/$', user_profile, name='user-profile'),
    url(r'^update-confirmation/$', update_confirmation, name='update-confirmation'),
    url(r'^register-confirmation/$', register_confirmation,
        name='register-confirmation'),
    url(r'^add-dict/$', add_dict, name='add-dict'),
    url(r'^/accts/$', accts, name='accts'),
    url(r'^', dashboard, name='dashboard'),



]
