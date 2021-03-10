from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.template.loader import get_template
import time


# Create your views here.

# 不定长参数
def test(request, **kwargs):
	# three/test1 会在访问的路径后面加上
	# / 表示根路径
	# redirect:重定向页面
	# reverse解析：根据name动态获得url地址
	return redirect(reverse('test1'))
	message = 'This is Three Test '
	if kwargs.get('time'):
		message += '<br>' + time.asctime(time.localtime(time.time()))
	return HttpResponse(message)


def test1(request, **kwargs):
	message = 'This is Three Test1 '
	if kwargs.get('time'):
		message += '<br>' + time.asctime(time.localtime(time.time()))
	return HttpResponse(message)


# def template_1(request, **kwargs):
# 	# 模拟用户登录后的响应的页面
# 	massage = '请先登录！！'
# 	username = 'yige'
# 	if username:
# 		message = f'<div>欢迎登陆<span style="color:red">{username}</span></div>'
# 	"""
# 		但是我们的页面肯定不止这一行html代码，如果都写在一个字符串里面就非常的复杂和臃肿
# 		那我们写普通的html页面可以吗？不可以
# 		于是django就给我们提供了一个叫模板的技术
# 	"""
# 	# 使用django.template.loader里面的get_template加载模板
# 	# get_template()函数得到模板文件，返回的Template对象
# 	t = get_template('three/template_1.html')
# 	print(t)
# 	# 使用它的render()方法,进行编译,可以传入参数,会将参数传入到模板文件中
# 	html = t.render({'username': username})
# 	print(html)
# 	return HttpResponse(html)


def template_2(request, **kwargs):
	username = '一个'
	"""
		render()是一个函数
		@:param request 请求对象
		@:param string 模板地址
		@:param [dict] 传递给模板的数据
	"""
	return render(request, 'three/template_1.html', {'username': username})


def fun():
	return 'function'


class Student:
	def __init__(self, name):
		self.name = name

	def study(self):
		return 'good good study'


def template_var(request, **kwargs):
	stu = Student('一个')
	context = {
		'int_var': 1,  # 整数
		'str_var': 'string',  # 字符串
		'fun_var': fun,  # 函数体
		'student_stu_var': stu.study,  # 方法
		'student_var': stu,  # 对象
		'list_var': [1, 2, 3],  # 列表
		'tuple_var': ('a', 'b', 'c'),  # 元组
		'dict_var': {'a': 1, 'b': 2, 'c': 3}  # 字典
	}
	return render(request, 'three/template_var.html', context)


def index(request, username, password, **kwargs):
	username_db = 'yige'
	password_db = 'qwe123'
	massage = '请先登录'
	context = {
		'username': massage,
		'password': massage
	}
	# select 'username','password' from 'user' where
	if username == username_db and password == password_db:
		context['username'] = username
		context['password'] = password
	return render(request, 'three/index.html', context)
