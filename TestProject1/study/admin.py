# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from study.models import Question, Choice
from django.contrib.admin.templatetags.admin_list import admin_list_filter

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_test']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
        ]
    inlines = [ChoiceInline]  #Choice 모델 클래스 같이 보기 
    list_display = ('question_test', 'pub_date', 'id')
    search_fields = ['question_test', 'id']
    
admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)