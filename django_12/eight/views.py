from django.shortcuts import render
from django.http import HttpResponse
from seven.models import User  # from APP名称.文件名 import 类名
from django.db.models import Count, Avg, Max, Min, Sum, F, Q
from .models import Product


# Create your views here.
# 常用的查询方法
def find(request):
	# 获取所有数据
	# rs = User.objects.all()

	# 获取第一条数据
	# rs = User.objects.first()

	# 获取最后一条数据
	# rs = User.objects.last()

	# 获取指定条件的数据
	# rs = User.objects.filter(age = 18)

	# 获取唯一的一条数据
	# rs = User.objects.get(id=7) # get返回的对象具有唯一性，如果符合条件的对象有多个则get报错，可以使用try处理

	# 对结果排序
	# rs = User.objects.order_by('age')
	# rs = User.objects.order_by('-age')  # 反向排序

	# 多项排序
	# rs = User.objects.order_by('age', '-id')

	# 获取当前查询到的数据的总数
	# rs = User.objects.all().count()
	# rs = User.objects.filter(age=18).count()

	# 将返回的QuerySet中的Model转字典
	# rs = User.objects.all().values()
	# for i in rs:
	# 	print(i['name'])

	# 常用查询条件
	# 相当于where语句后面的提交，传给查询方法的一些参数
	# 等于
	# rs = User.objects.filter(age=18)
	# 包含 模糊查询  like
	# 语法规则：字段名__条件，注意是两个下划线
	# rs = User.objects.filter(name__contains='个')

	# 大于
	# rs = User.objects.filter(age__gt=18)
	# 大于等于
	# rs = User.objects.filter(age__gte=18)
	# 小于
	# rs = User.objects.filter(age__lt=18)
	# 小于等于
	# rs = User.objects.filter(age__lte=18)

	# 是否为空
	# rs = User.objects.filter(city__isnull=True)

	# 以什么开始
	# rs = User.objects.filter(name__startswith='y')

	# 以什么结尾
	# rs = User.objects.filter(name__endswith='个')

	# 多个条件 成员属性 or
	# rs = User.objects.filter(name__in=['一个', '两个', '四个'])

	# 范围 闭区间 包含开头和结尾
	# rs = User.objects.filter(age__range=(18,28))
	# print(rs)

	# 聚合查询
	# 可以使用聚合函数进行聚合查询：Count、Avg、Max、Min、Sum
	# aggregate()是QuerySet的一个终止子句，返回的是一个包含键值对的字典
	# 统计条数
	# rs = User.objects.all().aggregate(Count('age'))

	# 求年龄平均值
	# rs = User.objects.all().aggregate(Avg('age'))

	# 求年龄最大值
	# rs = User.objects.all().aggregate(Max('age'))
	# 求年龄最小值
	# rs = User.objects.all().aggregate(Min('age'))
	# 年龄求和
	# rs = User.objects.all().aggregate(Sum('age'))

	# 可以修改key的值
	# rs = User.objects.all().aggregate(ageSum=Sum('age'))

	# 分组查询
	# 为调用的QuerySet中每个对象都生成一个独立的统计值
	# 拿出需要分组的字段，values方法能得到表中该字段的所有的数据
	# rs = User.objects.values('age')

	# 对age这个字段进行分组
	# rs = rs.annotate(count=Count('age'))

	# rs = User.objects.values('age').annotate(count=Count('age'))

	# F查询: F('xxx') 得到当前这个字段的值
	# 给User表中的所有人加一岁
	# rs = User.objects.all().update(age=F('age')+1)

	# Q查询   逻辑运算
	# 如果需要执行更加复杂的查询，可以使用Q查询
	# &(and) |(or) ~(not)
	# 查询名字为三个或者年龄为28为的用户  or
	# rs = User.objects.filter(Q(name='三个') | Q(age=28))

	# 查询名字为三个，并且年龄不等于28  and not
	rs = User.objects.filter(Q(name='三个') & ~Q(age=28))
	print(rs)
	return HttpResponse('查询成功')


def product(request, page):
	context = {}
	if page == 'list':
		context['productlist'] = list(Product.objects.all())
	return render(request, f'eight/product{page}.html',context)


def product_add(request):
	# 处理请求
	args = {
		'name': request.GET.get('name'),
		'price': request.GET.get('price'),
		'cover_map': request.GET.get('cover_map'),
		'link': request.GET.get('link')
	}
	Product.objects.get_or_create(**args)
	return HttpResponse('添加成功')
