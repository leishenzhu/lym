from django import template
from datetime import datetime

register = template.Library()  # 得到注册对象


# 把register.filter()用做装饰器
# name参数可以省略，如果没有声明name参数，django将使用函数名作为过滤器名称
# @register.filter('sex_change')  # 自定义过滤器
@register.filter
def sex_change(sex):
	if sex == 0:
		return '男'
	elif sex == 1:
		return '女'
	else:
		return '未知'

@register.filter
def isnull(value):
	return '' if value == None else value


# 我们可以传入参数
@register.filter
def change(value, args):
	return '未知' if value >= len(args) or value < 0 else args[value]


# 自定义简单（模板）标签
@register.simple_tag
def current_time():
	"""
		year
		month m
		m M
	"""
	format_string = '%Y年%m月%d日 %H:%M:%S'
	return datetime.now().strftime(format_string)


@register.simple_tag
def current_time_strf(format_string, a):
	print(a)
	return datetime.now().strftime(format_string)


# 还可以从上下文（视图）中获取传入的参数，注册标签的时候使用takes_context
@register.simple_tag(takes_context=True)
def current_time_context(context):
	format_string = context.get('format_string')
	return datetime.now().strftime(format_string)


# 包含标签,指定对应页面
@register.inclusion_tag('six/for_iter.html', takes_context=True)
def for_iter(context, key):
	# print(key)
	li = context.get(key)
	# 返回字典对象，key为要迭代的变量名
	return {'item': li}


"""
	使用register.filter()方法进行注册
	需要两个参数
	@param filtername 过滤器的名称
	@param funcname 编译的函数
"""
# register.filter('sex_change', sex_change)
