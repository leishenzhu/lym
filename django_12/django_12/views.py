from django.http import HttpResponse

"""
	用户发送的数据信息存储在HTTP请求当中
	所以我们需要得到用户发送的数据和信息就需要得到HTTP请求
	Django框架中，将HTTP请求封装成request对象，自动传入视图函数的第一个参数当中
	类似学习面向对象的时候
		class User:
			def __init__(self,name):
				self.name = name
		user = User('a')
	所以定义变量request，接受请求
"""
"""
	处理请求：
		处理客户端提交过来的数据
		比如：获取用户名，密码
"""
"""
	有了请求之后我们需要给用户进行响应，将资源返回给客户端
	1.导入HttpResponse对象
	2.通过return关键字进行返回
	处理响应：
		模型，去数据库查
		模板，渲染
"""


def test(request):
	text = 'Hello Django'
	return HttpResponse(text)


def course(request, name):
	return HttpResponse(f'学习{name}课程')


def testRepath(request, var):
	return HttpResponse(f're_path学习，测试{var}')
