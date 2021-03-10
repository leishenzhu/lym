from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def index_view(request):
    #获取当前请求方式（GET/POST）
    m =  request.method

    if m=='GET':
        return render(request,'register.html')
    else:
        #获取请求参数
        uname = request.POST.get('uname','')
        pwd = request.POST.get('pwd','')

        #判断
        if uname and pwd:
            #创建模型对象
            stu = Student(sname=uname,spwd=pwd)
            #插入数据库
            stu.save()

            return HttpResponse('注册成功')
        return HttpResponse('注册失败！')