from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from django.shortcuts import redirect, reverse, render


# 方法一
# 异常中间件
class MyException(MiddlewareMixin):

	def process_exception(self, request, exception):
		print('自定义异常中间件')
		# return HttpResponse(f'发生异常：{exception}')
		# return redirect(reverse('twelve_test1'))
		return render(request, 'twelve/error.html', {'message': exception})


# 方式二
# 登录中间件
class UserMiddleware:
	# 将相应的视图函数封装在get_resp中
	def __init__(self, get_resp):
		self.get_resp = get_resp

	# 实例对象调用()，执行这个方法,必须响应
	# 在视图函数执行前调用，此方法做登录的拦截
	def __call__(self, request):
		print(request.path)
		# 不允许拦截的路由
		no_treatment_li = ['/eleven/page/login/', '/eleven/login/']
		if request.path not in no_treatment_li:
			username = request.session.get('username', None)
			if not username:
				return render(request, 'eleven/login.html')
		print('在视图函数之前执行')
		# 调用本身的视图函数，保存return的对象
		response = self.get_resp(request)
		print('在视图函数之后执行，可以对响应做处理')
		return response
