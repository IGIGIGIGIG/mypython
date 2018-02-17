# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from books.models import Book, Author, Publisher




# Create your views here.

#-- TemplateView
class BooksModelView(TemplateView):
    template_name = 'books/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(BooksModelView, self).get_context_data(**kwargs)
        context['object_list'] = ['Book', 'Author', 'Publisher']
        return context
    
#-- ListView
class BookList(ListView):
    model = Book
#디폴트로 지정해 주는 옵션이 있다. context 변수로 object_list를 지정해 주는 것과, 템플릿 파일을 """모델명소문자_list.html"""로 지정 해 주는 것.
    
class AuthorList(ListView):
    model = Author
    
class PublisherList(ListView):
    model = Publisher
    
#-- DetailView
class BookDetail(DetailView):
    model = Book

class AuthorDetail(DetailView):
    model = Author
    
class PublisherDetail(DetailView):
    model = Publisher


