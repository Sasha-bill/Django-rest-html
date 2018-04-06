# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

import requests
from lxml import html
from collections import Counter
import json


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        url_enter = request.POST.get("url_enter")    # enter url name

        page = requests.get(url_enter)
        tree = html.fromstring(page.content)

        all_elms = tree.cssselect('*')
        all_tags = [x.tag for x in all_elms]

        c = Counter(all_tags)

       # print('all:', len(all_elms), 'span:', c['span'])  # if need all to count all tags

        d = {}
        for e in c:
            d[e] = c[e]

        j = json.dumps(d, sort_keys=True, indent=4)
      #  print(j)   # for terminal output

        return HttpResponse("<h2>Hello, {0} <p>We counted your HTML code tags:<p> {1} </p> </p></h2>".format(name, j))
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})
