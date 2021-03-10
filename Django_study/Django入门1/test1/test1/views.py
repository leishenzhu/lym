#coding=utf-8

# 显示hello world
from django.http import HttpResponse


def index_view(request):
	return HttpResponse('hello world')