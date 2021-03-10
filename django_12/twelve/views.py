from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def test(request):
	# 1 / 0
	print('首页')
	return HttpResponse('首页')


def test1(request):
	# 1 / 0
	print('用户信息页')
	return HttpResponse('用户信息页')
