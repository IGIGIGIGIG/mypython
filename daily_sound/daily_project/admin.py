# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from daily_project.models import *
# Register your models here.
    
admin.site.register(user)
admin.site.register(VideoCategory)
admin.site.register(video)
