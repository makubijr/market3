from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','market.views.home',name="home"),
    url(r'^lib/','profiles.views.library',name="library"),
    url(r'^products/',include('products.urls')),
    url(r'^cart/',include('cart.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

)
