from django.conf.urls import patterns, include, url
from graphapp.views import home

urlpatterns = patterns('',
    url('^$', home),
)
