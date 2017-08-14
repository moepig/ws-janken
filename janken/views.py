# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from channels import Group
from django.views.generic import TemplateView
from django.http import HttpResponse

class LobbyView(TemplateView):
    template_name = "janken/lobby.html"


def publish(request):
    msg = request.GET.get('msg', 'is null')
    Group("sample").send({'text': msg})

    return HttpResponse("published!")