from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lighten.views.home', name='home'),
    # url(r'^lighten/', include('lighten.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('', 
    url(r'^serverlog/$', 'applogsys.views.serverlog', name='serverlog'),
    url(r'^loginlog/$', 'applogsys.views.loginlog', name='loginlog'),
    url(r'^faultlog/$', 'applogsys.views.faultlog', name='faultlog'),
)
