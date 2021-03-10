from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django_12.settings import MEDIA_ROOT
import os, time
from nine.models import Student


# Create your views here.
def httpRequestTest(request):
	# 通过属性获取请求信息
	print(request.path)  # 请求路径
	print(request.method)  # 请求方法
	print(request.encoding)  # 编码格式,None为默认设置，一般utf-8
	return HttpResponse('执行成功')


def get_post(request):
	# 根据请求方式执行对应的功能
	# get请求，响应模板页面
	if request.method == 'GET':
		# get的提交方式，django会把用户填写表单提交的数据保存GET属性当中
		# GET属性保存的是一个QueryDict对象类型，和字典类似
		print('GET', request.GET)
		return render(request, 'ten/get_post.html')
	elif request.method == 'POST':
		# post的提交方式，表单的数据如何获取？和GET类型，会把用户填写表单提交的数据保存POST属性当中
		print('POST', request.POST)
		print('username', request.POST.get('username'))
		print('password', request.POST.get('password'))
	# print('hobby', request.POST.get('hobby'))
	# print('hobby', request.POST.getlist('hobby'))

	# 也可以转字典进行操作
	# print(dict(request.POST)['hobby'])
	return HttpResponse('执行成功')


def page(request, page):
	return render(request, f'ten/{page}.html')


class UserView(View):
	def get(self, request):
		print('GET', request.GET)
		return render(request, 'ten/get_post.html')

	def post(self, request):
		print('POST', request.POST)
		print('username', request.POST.get('username'))
		print('password', request.POST.get('password'))
		print('hobby', request.POST.getlist('hobby'))
		return HttpResponse('POST执行成功')


class Upload(View):
	def post(self, request):
		# 得到请求中的文件的数据
		files = request.FILES.get('file')
		# 返回的是一个实例对象
		# print(files, type(files))

		# 使用chunks()方法得到文件中的数据
		# print(files.chunks())
		# for i in files.chunks():
		#     print(i)

		# 所以我们在服务器创建一个文件，文件名为上传的文件，然后将数据写入进去，就完成了文件上传
		# 处理文件名，防止重名
		files_name = ''.join(str(time.time()).split('.')) + files.name
		files_path = os.path.join(MEDIA_ROOT, files_name)
		with open(files_path, 'wb') as f:
			for i in files.chunks():
				f.write(i)
		return HttpResponse('上传成功')


class Result:
	# 常见的状态码
	code = {
		'success': 200,
		'error': 500
	}

	def diy_res(self, msg, data, code=None):
		code = code if code else self.code[msg]
		# 'ensure_ascii': False  设置json中的汉字编码
		return ({'code': code, 'msg': msg, 'data': data}, {'ensure_ascii': False})


rs = Result()


class StudentView(View):
	def get(self, request):
		# values()：把student对象转成属性与属性值为键值对形式
		student_list = list(Student.objects.all().values())
		# res, json_dumps_params = rs.diy_res('提取失败', student_list, code=104)
		res, json_dumps_params = rs.diy_res('success', student_list)
		return JsonResponse(res, json_dumps_params=json_dumps_params)
