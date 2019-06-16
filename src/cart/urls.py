from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('cart.views',
        url(r'^$','cart',name="cart"),
        url(r'^update_cart/(?P<id>.*)','update_cart',name="update_cart"),
)
