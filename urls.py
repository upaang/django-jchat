from django.conf.urls.defaults import *
import settings

from views import index, simple, complex


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^django_jchat/', include('django_jchat.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
    (r'^$', index),
    (r'^simple$', simple),
    (r'^complex/(?P<id>\d)$', complex),
    (r'^chat/', include('jchat.urls')),
    (r'^accounts/login/', 'django.contrib.auth.views.login', {'template_name':'login.html'}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)
