from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()


def make_an_error(request):
    raise Exception

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    # url(r'^example/', include('example.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^error/?', make_an_error),
    url(r'^admin/', include(admin.site.urls)),
)
