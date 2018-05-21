# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from main.models import Goods
# Create your views here.
def main_page(request):
    goods = Goods.objects.all()
    return render(request,"hello.html", locals())