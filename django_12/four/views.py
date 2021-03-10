from django.shortcuts import render
from datetime import datetime


# Create your views here.
def filter_var(request):
	context = {
		'str_var': 'THIS IS PYTHON',
		'now': datetime.now,
		'name': '<span style="color: red">yige</span>'
	}
	return render(request, 'four/filter_var.html', context)


def static_file(request):
	return render(request, 'four/static_file.html')


class User:
	def __init__(self, name, age, sex=0):
		self.name = name
		self.age = age
		self.sex = sex


def template_label(request):
	# 0男 1女
	user = User('一个', 18, 0)
	# user = None
	context = {
		'user': user
	}
	return render(request, 'four/template_label.html', context)
