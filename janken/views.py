# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from channels import Group
from django.views.generic import TemplateView
from django.http import HttpResponse


class LobbyView(TemplateView):
    template_name = "janken/lobby.html"


def publish(request):
    msg = request.GET.get('msg', 'is null')
    Group("1").send({'text': msg})

    return HttpResponse("published!")


class MatchView(TemplateView):
    template_name = "janken/match.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context["room_id"] = kwargs.get("room_id", "undefined")

        return context

