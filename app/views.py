# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        url_enter = request.POST.get("url_enter")


        return HttpResponse("<h2>Hello, {0}, \n we counted your HTML code tags: {1}  </h2>".format(name, url_enter))
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})
