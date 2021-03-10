from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def template_label(request):
	context = {
		'course': ['python', 'linux', 'mysql', 'redis', 'mongdb', 'socket', 'process', 'thread', 'html', 'css', 'js',
				   'jquery', 'django'],
		'int': 1,
		'course_info': ('难点', '周边'),
		'html_text': '<div>有html标签的哦</div>',
	}
	return render(request, 'five/template_label.html', context)


def url_var(request, var):
	return render(request, 'five/url_var.html', {'var': var})


def index(request, value):
	return render(request, f'five/index{value}.html')
