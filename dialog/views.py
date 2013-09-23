# -*- coding: utf-8 -*-
from models import Conversation, Category, Dialog
from django.shortcuts import render_to_response
from django.template import RequestContext



def conversation_view(request, dialog_id):
    print dialog_id
    conversation = Conversation.objects.get(pk = 1)
    context = RequestContext(request)
    return render_to_response("dialog/conversation.html", context)

def new_conversation_view(request):
    if request.method == "POST":
        new_conversation = Conversation()
        new_conversation.title = request.POST.get("title", "title not found")
        if request.POST.get("category", "") != "":
           new_conversation.category = Category.objects.get(pk = int(request.POST.get("category")))
        new_conversation.save()
    categories = Category.objects.all()
    context = RequestContext(request, {
        "categories": categories
    })
    return render_to_response("dialog/form_conversation.html", context)
