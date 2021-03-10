from django.shortcuts import render, reverse, redirect
from django.http import FileResponse, HttpResponse
from django_12.settings import MEDIA_ROOT
import os, datetime
from django.views import View
from .forms import RegisterForm
from .models import User

# Create your views here.
def download(request):
	# 实际情况存在数据库当中
	name = '161189801361179021.jpg'
	file_name = os.path.join(MEDIA_ROOT, name)
	# 获取文件数据
	file = open(file_name, "rb")
	# 实例化文件响应对象
	response = FileResponse(file)
	# 设置响应头
	response['Content_Type '] = 'application/octet-stream'
	response['Content-Disposition'] = f'attachment;filename={name}'

	return response


def set_cookie(request):
	# 实例化响应对象
	response = HttpResponse('设置cookie')
	# 通过响应头，set_cookie 服务器往客户端设置数据
	# response.set_cookie('username', 'yige') # 默认关闭浏览器过期
	# 设置过期时间s max_age:x秒
	response.set_cookie('username', 'yige', max_age=60 * 60 * 24 * 3)  # 默认关闭浏览器过期
	response.set_cookie('password', 'qwe123', max_age=60 * 60 * 24 * 3)  # 默认关闭浏览器过期
	# 指定过期时间  csrf攻击
	# response.set_cookie('username', 'yige', expires=datetime.datetime(2021, 1, 30, 5, 53))  # 默认关闭浏览器过期

	return response


def get_cookie(request):
	cookie = request.COOKIES
	username = cookie.get('username')

	if username:
		return HttpResponse(f'欢迎：{username}')
	else:
		return HttpResponse('请登录')


def delete_cookie(request):
	resposne = HttpResponse('删除cookie')
	resposne.delete_cookie('username')
	return resposne


class Page(View):
	def get(self, request, page):
		context = {}
		if page == 'logout':
			return redirect(self.logout(request))
		elif page == 'register':
			# 实例化注册表单
			context['form'] = RegisterForm()
		context['username'] = request.session.get('username', None)

		return render(request, f'eleven/{page}.html', context)

	def logout(self, request):
		request.session.flush()
		return reverse('eleven_page', kwargs={'page': 'login'})


class Login(View):
	def post(self, request):
		# 获取账户密码
		username = request.POST.get("username")
		# 数据库查询校验
		# 登陆成功状态保持  session类字典
		request.session['username'] = username  # 如果没有指定过期时间，默认是两个星期后过期
		request.session.set_expiry(10)  # value是一个整数，会话将在value秒后没有活动过期
		request.session.set_expiry(datetime.datetime(2021, 1, 31, 12, 32))  # 指定时间国企，注意：一定要序列化setting.py中
		request.session.set_expiry(0)  # 0关闭浏览器则过期
		request.session.set_expiry(None)  # None永不过期

		return redirect(reverse('eleven_page', kwargs={'page': 'index'}))


class RegisterView(View):
	def post(self, request):
		form = RegisterForm(request.POST) # 获取form表单的数据
		if form.is_valid(): # 验证数据是否合法
			# 拿数据
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			password_repeat = form.cleaned_data['password_repeat']
			email = form.cleaned_data["email"]

			if password==password_repeat:
				User.objects.create(username=username, password=password,email=email)
				return redirect(reverse('eleven_page', kwargs={'page': 'login'}))
			else:
				return HttpResponse('两次密码不一致')
		else:
			return HttpResponse('注册失败')
