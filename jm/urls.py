from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from libs.views import *
from blog.views import *

admin.autodiscover()

urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": {"cmspages": CMSSitemap}}),
]


urlpatterns += i18n_patterns(
    path("accounts/profile/", dash, name='dash'),
    path("accounts/", include('allauth.urls')),
    path("libs/", include('libs.urls')),
    path("mail/", mail, name='mail'),
    path("secure/", admin.site.urls), 
    path("taggit_autosuggest/", include('taggit_autosuggest.urls')),
    path("", include("cms.urls")))

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
