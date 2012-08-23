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
    url(r'^$','appinfosys.views.index',name='sysinfoindex'),
    url(r'^hosts/$','appinfosys.views.hosts',name='sysinfohosts'),
    url(r'^cpu/$','appinfosys.views.cpu',name='sysinfocpu'),
    url(r'^disk/$','appinfosys.views.disk',name='sysinfodisk'),
    url(r'^network/$','appinfosys.views.network',name='sysinfonetwork'),
    url(r'^ipnet/$','appinfosys.views.ipnet',name='sysinfoipnet'),
    url(r'^ipnet/ipadd/$','appinfosys.views.ipadd',name='sysinfoipadd'),
)
