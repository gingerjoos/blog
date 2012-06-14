from django.conf.urls import patterns, include, url

urlpatterns = patterns('content.views',
               url(r'^(.*)/(.*)$','view_post',name='view post'),
              )
