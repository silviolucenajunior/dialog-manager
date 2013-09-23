# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('dialog.views',
    url(r'^conversation/dialog/(?P<dialog_id>.*)/$', 'conversation_view'),

    #Conversation focus view
    url(r'^conversation/new-conversation/$', 'new_conversation_view'),
)
