from django.shortcuts import render
# coding:utf-8
from django.http import HttpResponse


def index(request):
    return render(request, 'home.html')