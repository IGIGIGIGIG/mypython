# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# 데이터베이스 모델하는 django의 파일
# Create your models here.
class Question(models.Model):
    question_test = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self): #__str__ onPython 2.7
        return self.question_test
    
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    
    def __unicode__(self): #__str__ on Python2.7
        return self.choice_text
    
class test(models.Model):
    hello_world = models.CharField(max_length = 200)
    
    def __unicode__(self):
        return self.hello_world