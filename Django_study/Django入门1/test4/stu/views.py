from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def index_view(request):
	# 根据不同的请求方式处理不同的业务需求
	if request.method=='GET':
		return render(request,'register.html')
	else:
		#1.接收请求参数
		uname = request.POST.get('uname','')
		pwd = request.POST.get('pwd','')

		#2.非空判断
		if uname and pwd:
			# 3.创建模型对象
			student = Student(sname=uname,spwd=pwd)
			# 4.插入数据库
			student.save()
			#5.页面响应
			return HttpResponse('注册成功')
		return HttpResponse('注册失败')


def show_view(request):
	# 1.查询stu_student表中的所有数据
	stus = Student.objects.all()

	return render(request,'show.html',{'students':stus})


def login_view(request):
	if request.method =='GET':
		return render(request,'login.html')
	else:
		#1.获取请求参数
		uname = request.POST.get('uname')
		pwd = request.POST.get('pwd')

		#2.查询数据库
		if uname and pwd:
			c = Student.objects.filter(sname=uname,spwd=pwd).count()

			#3.判断是否登陆成功
			if c==1:
				return HttpResponse('登陆成功！')
		return HttpResponse('登陆失败！')