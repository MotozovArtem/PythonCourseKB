# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from main.models import Goods
# Register your models here.

class GoodsAdmin(admin.ModelAdmin):
    model=Goods
    list_display = ['name', 'price']

admin.site.register(Goods, GoodsAdmin)