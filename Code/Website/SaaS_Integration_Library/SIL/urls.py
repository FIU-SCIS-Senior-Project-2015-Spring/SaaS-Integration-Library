from django.conf.urls import patterns, url
from SIL import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^api/$', views.datasets, name='datasets'),
                       url(r'^api/(?P<api_name>\w+)/$', views.api, name='api'),
                       url(r'^api/(?P<api_name>\w+)/(?P<action_name>\w+)$', views.apicall, name='apicall'))

