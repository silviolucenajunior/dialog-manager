# -*- coding: utf-8 -*-
from models import Conversation


def conversation_view(id):
    conversation = Conversation.objects.get(id = (int)id)