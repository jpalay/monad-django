from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from content.views import display_page
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'monad.views.home', name='home'),
    # url(r'^monad/', include('monad.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

#     url(r'^accounts/login/$', 'django.contrib.auth.views.login', {
#     	'template_name': 'login.html'
#     }),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^$', RedirectView.as_view(url='/1/')),
    url(r'^(?P<slug>.+)/$', 'content.views.display_page', name="display_page"),
)
