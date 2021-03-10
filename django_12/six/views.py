from django.shortcuts import render


# Create your views here.
class User:
	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex


# 自定义过滤器
def custom_filter(request):
	user = User('一个', 18, 0)
	context = {
		'user': user,
		'sex_li': ['男', '女'],
		'label_index': 1,
		'label_list': ['java', 'python', 'c'],
		'format_string': '%Y年%m月%d日 %H:%M:%S',
		'course': ['python', 'linux', 'mysql', 'redis', 'mongodb', 'socket']
	}
	return render(request, 'six/custom_filter.html', context)

