# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from books.models import Book, Author, Publisher
# Register your models here.


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
