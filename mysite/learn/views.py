# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.db import models

def index(request):
    return HttpResponse(u"欢迎光临 自强学堂")


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def htmlIndex(request):
    return render(request, 'home.html')

def homeTest(request):
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    return render(request, 'home.html', {'TutorialList': TutorialList})


#python 类的继承写法
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
# Create your views here.
