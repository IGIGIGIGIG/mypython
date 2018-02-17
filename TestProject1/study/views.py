# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from study.models import Question, Choice
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from Explorer.Standard_Suite import selected_text
from django import forms
from django.http import HttpResponse
from django.views.generic import View
from anaconda_navigator.utils.py3compat import request
# from study.foms import NameForm
    
    
    ###현제 에러가 안나게 만든 class
class MyView(View):
    def get(self, request):
        #뷰 로직 작성
        return HttpResponse('result')

  
    

# Create your views here.
def index(request):#request는 뷰 함수의 필수 인자임 ㅇㅇ
#     return HttpResponse("hello world")
    latest_question_list = Question.objects.all().order_by('-pub_date')[:25]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'study/index.html', context)

def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'study/detail.html', {'question':question})

def vote(request, question_id):#line 4
    p = get_object_or_404(Question, question_id) #line 5
    try : #line 5 
        selected_choice = p.choice_set.get(pk=request.POST['choice']) #line5 choice테이블을 검색, 검색 조건은 pk=request.POST['choice']
    except(KeyError, Choice.DoesNotExist): #line 6
        #설문 투표 폼을 다시 보여준다.
        return render(request, 'study/detail.html', {#line 7
            'question' : p, #line 7
            'error_message' : "you didn't select a choice.", #line 7
        })#line 7
        
    else:#line 8
        selected_choice.votes += 1 #line 9
        selected_choice.save() # line 10
        #POST 데이터를 정상적으로 처리하였으면,
        #항상 HttpResponseRedirect를 반환하여 리다이렉션 처리함...
        return HttpResponseRedirect(reverse('study:results', args=(p,id,))) #line 11,12 -- vote() 뷰 함수가 리다이렉트 할 타겟 url을 담은 HttpResponseRedirect반환 
                                                                            #POST방식의 폼 데이터를 처리하는경우,HttpResponseRedirect 객체를 리턴하는 것이 일반
                                    #reverse() 함수 사용하여 url 패턴으로부터 url 스트링을 구할 수 있다.

           
def results(request, question_id):#line2
    question = get_object_or_404(Question, pk=question_id)#line 4
    return render(request, 'study/results.html', {'question':question}) #line 5,6





# def get_name(request):
# #    post방식이면, 데이터가 담긴 제출된 폼으로 간주
#     if request.method == "POST": 
#         form = NameForm(request.POST)#request에 담긴 데이터로, 클래스 폼을 생성합니다.
#         #폼에 담긴 데이터가 유효한지 체크합니다.
#         if form.is_valid():
#             #폼 데이터가 유효하면, 데이터는 cleaned_data로 복사됩니다.
#             new_name = form.cleaned_data['name']
#             #로직에 따라 추가적인 처리를 합니다.
#             
#             #새로운 url로 리다이렉션 시킵니다.
#             return HttpResponseRedirect('/thanks/')
#         
#     #post 방식이 아니면 (보통은 get임),
#     #빈 폼을 사용자에게 보여줍니다.
#     else:
#         form = NameForm()
#         
#     return render(request, 'name.html', {'form':form})
#         
        
        
