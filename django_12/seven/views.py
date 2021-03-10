from django.shortcuts import render
from django.http import HttpResponse
from .models import User


# Create your views here.
def user_add(request):
	# 处理请求
	# 处理响应
	# 方式一
	user = User(name='yige', age=18)  # 创建实例对象
	user.save()  # 使用save()方法保存添加

	# 方式二
	# user = User()
	user.name = '两个'
	user.age = 28
	user.save()

	# 方式三
	User.objects.create(name='三个', age=18)

	# 方式四 get_or_create()会判断有没有你传入的数据，如果有则不创建，只获取；如果没有创建，并获取。返回一个元组
	# rs = User.objects.get_or_create(name='三个',age=28)
	user, flag = User.objects.get_or_create(name='三个', age=28)
	# user, flag = User.objects.get_or_create(name=name, age=age)
	message = '添加成功'
	if not flag:
		message = '已有数据'
	print(user.name, user.age, user.create_time)
	return HttpResponse(message)


def user_find(request):
	# 查询所有
	# user_list = User.objects.all()
	# print(user_list)  # 返回QuerySet对象

	# 查询一个记录 get用来查询唯一数据的，有多个数据会报错，一般用于id
	user = User.objects.get(id=6)
	print(user, type(user))

	# 查询满足条件的对象 筛选
	# user_list = User.objects.filter(age=18)
	# print(user_list, type(user_list))

	# QuerySet是可迭代对象
	# user_list = User.objects.all()
	# for user in user_list:
	# 	print(user)

	# QuerySet支持切片 包前不包后
	# print(user_list[0:2])
	# 转型
	# print(list(user_list))

	return HttpResponse('查询成功')


def user_update(request):
	# 修改单个数据，先查找到对象，再修改属性（属性赋值修改）
	# try:
	# 	user = User.objects.get(name='四个')
	# 	# print(user.name, user.age, user.create_time)
	# 	user.age = 18
	# 	user.save()	 # 保存更新
	# except Exception as e:
	# 	return HttpResponse('修改失败，get获取了多条')

	# 修改多条，使用filter查找多条
	# user_list = User.objects.filter(name='三个')
	# print(user_list)
	# for user in user_list:
	# 	user.age = 18
	# 	user.save()

	# User.objects.filter(name='三个').update(age=28) # auto_now只有使用save方法才会将当前时间修改进去

	# 使用all查找所有
	User.objects.all().update(city='长沙')

	return HttpResponse('修改成功')


def user_del(request):
	# 删除单个
	# User.objects.get(id=5).delete()

	# 删除多个
	# User.objects.filter(age=28).delete()

	# 删除所有
	User.objects.all().delete()

	# 先找到要修改的数据，在修改（方式一：该属性，save方法保存；方式二：直接使用QuerySet.update修改）
	return HttpResponse('删除成功')
