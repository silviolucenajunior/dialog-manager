# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('dialog.views',
    url(r'^conversation/(?P<id>).*/$', 'conversation_view'),
)
