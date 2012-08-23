from django.conf.urls.defaults import patterns, include, url
import settings
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
    url(r'^$','lighten.views.index'),
    url(r'^index/$','lighten.views.index'),
    url(r'^quit/$','lighten.views.quit'),
    url(r'^infosys/',include('lighten.appinfosys.urls'),name='sysinfonum'),
    url(r'^applogsys/',include('lighten.applogsys.urls'),name='appserverlog'),
    url(r'^media/(?P<path>.*)','django.views.static.serve',{'document_root': settings.STATIC_PATH}),
    url(r'^networksys/',include('lighten.appnetworksys.urls')),
    url(r'^assetsys/',include('lighten.appassetsys.urls'),name='assetsysinfo'),
    url(r'^monitorsys/',include('lighten.appmonitorsys.urls'),name='sysmontor'),
    url(r'^user/',include('lighten.appuser.urls'),name='puser'),
)

