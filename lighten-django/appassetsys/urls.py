#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lighten.views.home', name='home'),
    # url(r'^lighten/', include('lighten.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^hardinfo/$','appassetsys.views.hardinfo',name='assetsyshardinfo'),
    url(r'^hdinfo/$','appassetsys.views.hdinfo',name='assetsyshdinfo'),
    url(r'^uphdinfo/(?P<upsn>.*)/$','appassetsys.views.uphdinfo',name='assetsysuphdinfo'),
    url(r'^hdinsert/$','appassetsys.views.hdinsert',name='assetsyshdinsert'),
    url(r'^hdinfodel/(?P<delsn>.*)/$','appassetsys.views.hdinfodel',name='assetsyshdinfodel'),
    url(r'^searchhdinfo/$','appassetsys.views.searchhdinfo',name='assetsyssearchhdinfo'),
    url(r'^beloneinfo/$','appassetsys.views.beloneinfo',name='assetsysbeloneinfo'),
    url(r'^blinfo/$','appassetsys.views.blinfo',name='assetsysblinfo'),
    url(r'^fwqgsinsert/$','appassetsys.views.fwqgsinsert',name='assetsysfwqgsinsert'),
    url(r'^fwqgsup/(?P<gssn>.*)/$','appassetsys.views.fwqgsup',name='assetsysfwqgsup'),
    url(r'^fwqgsdel/(?P<gsdelsn>.*)/$','appassetsys.views.fwqgsdel',name='assetsysfwqgsdel'),
    url(r'^fwqgssearch/$','appassetsys.views.searchblinfo',name='assetsysfwqgssearch'),

)
