from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from tasaparo.web.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tasaparo.views.home', name='home'),
    # url(r'^tasaparo/', include('tasaparo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$',
        HomeView.as_view(),
        name = 'home',
    ),

    url(r'^api/', include('tasaparo.core.urls', namespace='api')),

    url(r'^admin/', include(admin.site.urls)),
)
