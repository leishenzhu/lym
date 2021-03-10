from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# 渲染登录首页
def index_view(request):
	return render(request, 'login.html')


def login_view(request):
	# 接收请求参数
	uname = request.GET.get('uname', '')
	pwd = request.GET.get('pwd', '')

	# 判断
	if uname == 'zhangsan' and pwd == '123':
		return HttpResponse('登陆成功')
	return HttpResponse('登陆失败')
