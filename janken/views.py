# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView


class LobbyView(TemplateView):
    template_name = "janken/lobby.html"
