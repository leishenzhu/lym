from django.shortcuts import render, redirect, reverse
from .models import Classes, Student, StudentDetails, Course
from django.db.models import Q


# Create your views here.
def page(request, index):
	classess_list_page = ['classes', 'student_add']
	context = {}
	if index in classess_list_page:
		classes_all(context)
	elif index == 'student':
		student_all(context)
	elif index == 'course':
		# 获取所有的课程数据
		context['course_list'] = list(Course.objects.all())
	return render(request, f'nine/{index}.html', context)


# 获取所有班级信息
def classes_all(context):
	classes_list = Classes.objects.all()
	context['classes_list'] = list(classes_list)


def student_all(context):
	# 获取所有学生信息
	student_list = Student.objects.all()
	# Student模型类中有定义classes属性，所有我们可以直接通过该属性去访问对应班级信息
	# print(student_list, student_list[0].classes.name)
	# 通过学生找学生详情，反向，会生成一个类名小写的属性，保存着关联表的数据
	# print(student_list[0].studentdetails.age)
	context['student_list'] = list(student_list)


def classes_add(request):
	# 处理请求
	id = request.GET.get('id')
	name = request.GET.get('name')
	slogan = request.GET.get('slogan')
	if id:
		# 修改
		classes = Classes.objects.get(id=id)
		classes.name = name
		classes.slogan = slogan
		classes.save()
	else:
		# 添加
		Classes.objects.get_or_create(name=name, slogan=slogan)

	# 处理响应
	return redirect(reverse('page', kwargs={'index': 'classes'}))


def classes_update(request, id):
	classes = Classes.objects.get(id=id)
	return render(request, f'nine/classes_add.html', {'classes': classes})


def classes_del(request, id):
	Classes.objects.get(id=id).delete()
	return redirect(reverse('page', kwargs={'index': 'classes'}))


def student_add(request):
	get = request.GET
	id = get.get('id')

	student = {
		'name': get.get('name'),
		'credit': get.get('credit'),
		'classes_id': get.get('classes'),
	}
	studentDetails = {
		'age': get.get('age'),
		'sex': get.get('sex'),
		'city': get.get('city'),
		'note': get.get('note'),
	}
	studentDetails['age'] = studentDetails['age'] if studentDetails['age'] != '' else None
	studentDetails['sex'] = studentDetails['sex'] if studentDetails['sex'] != '' else None
	studentDetails['city'] = studentDetails['city'] if studentDetails['city'] != '' else None
	studentDetails['note'] = studentDetails['note'] if studentDetails['note'] != '' else None

	if id:
		# 先得到学生对象
		student_obj = Student.objects.get(id=id)
		student_obj.name = student['name']
		student_obj.credit = student['credit']
		student_obj.classes_id = student['classes_id']
		student_obj.save()
		# 学生详情对象
		studentDetails_obj = StudentDetails.objects.get(student_id=id)
		studentDetails_obj.age = studentDetails['age']
		studentDetails_obj.sex = studentDetails['sex']
		studentDetails_obj.city = studentDetails['city']
		studentDetails_obj.note = studentDetails['note']
		studentDetails_obj.save()
	else:
		# 学生创建
		# 创建方式一：传入关联表的主键值，需要注意外键的值必须是关联表中已经存在的值
		# Student.objects.get_or_create(**student)
		student = Student(**student)
		student.save()
		# 创建方式二：用属性赋值的方式，模型类有定义一个student属性，而这个属性的对象类型是student表的实例对象
		studentDetails = StudentDetails(**studentDetails)
		studentDetails.student = student
		studentDetails.save()
	# 处理响应
	return redirect(reverse('page', kwargs={'index': 'student'}))


def student_del(request, id):
	Student.objects.get(id=id).delete()
	return redirect(reverse('page', kwargs={'index': 'student'}))


def student_update(request, id):
	student = Student.objects.get(id=id)
	classes_list = Classes.objects.all()
	context = {
		'student': student,
		'classes_list': classes_list
	}
	return render(request, f'nine/student_add.html', context)


def course_add(request):
	# 处理请求
	get = request.GET
	id = get.get('id')
	credit = get.get('credit')
	duration = get.get('duration')
	# 必填数据
	course = {
		'name': get.get('name')
	}
	# 选填数据
	if credit != "":
		course['credit'] = credit
	if duration != "":
		course['duration'] = duration

	print(course)
	if id:
		# 修改
		course_obj = Course.objects.get(id=id)
		course_obj.name = course['name']
		course_obj.credit = course['credit']
		course_obj.duration = course['duration']
		course_obj.save()
	else:
		# 添加
		Course.objects.get_or_create(**course)

	# 处理响应
	return redirect(reverse('page', kwargs={'index': 'course'}))


def course_update(request, id):
	course = Course.objects.get(id=id)
	return render(request, f'nine/course_add.html', {'course': course})


def course_del(request, id):
	Course.objects.get(id=id).delete()
	return redirect(reverse('page', kwargs={'index': 'course'}))


# 根据班级获取学生信息
def student_find_by_classes(request, id):
	'''
	管理器：
		如果模型A有一个ForeignKey，那么该ForeignKey所指的模型B实例可以通过一个管理器得到前面有ForeignKey的模型A的所有实例
		默认情况下，这个管理器的名字为：源模型的小写名称_set
	'''
	# 通过id得到班级
	classes = Classes.objects.get(id=id)
	print(classes)  # 班级实例对象
	print(classes.name)  # 班级名称

	# print(classes.student_set) # 反向的时候的一种管理器，里面包含了方法
	# print(classes.student_set.all())  # 使用all方法得到该班级的所有学生数据
	student_list = list(classes.student_set.all())
	return render(request, f'nine/student.html', {'student_list': student_list})


# 查询课程有哪些学生报名
def student_find_by_course(request, id):
	course = Course.objects.get(id=id)
	# 反向管理器 student_set
	student_list = list(course.student_set.all())
	context = {
		'course': course,
		'student_list': student_list
	}
	return render(request, f'nine/student_course.html', context)


def student_add_by_course(request, id):
	'''
		多表查询：它在后台自动帮你处理join
		只需要使用关联的模型字段的名称，并使用双下划线分割直到你想要的字段
	'''
	# 查询年龄为18的学生报名的所有课程
	# rs = Course.objects.filter(student__studentdetails__age=18)

	# 查询学生姓名包含‘个’的班级信息
	# rs = Classes.objects.filter(student__name__contains='个')

	# 查询报名了Linux的学生详情信息
	rs = StudentDetails.objects.filter(student__course__name='linux')
	print(rs.values())
	# 查询所有未报名该课程的学生
	student_list = Student.objects.filter(~Q(course__id=id))
	course = Course.objects.get(id=id)
	context = {
		'course': course,
		'student_list': student_list
	}
	return render(request, f'nine/student_course_add.html', context)


def course_add_student(request):
	get = request.GET
	course_id = get.get('course_id')
	# 多选框
	student_id = get.getlist('student_id')
	# print(course_id, student_id)

	# 给课程添加学生
	if student_id:
		course = Course.objects.get(id=course_id)
		student_list = list(Student.objects.filter(id__in=student_id))
		course.student_set.add(*student_list)
	return redirect(reverse('student_find_by_course', kwargs={'id': course_id}))


def course_del_student(request, course_id, student_id):
	# 课程移除学生
	# 课程实例
	course = Course.objects.get(id=course_id)
	# 要移除的学生实例
	student = Student.objects.get(id=student_id)
	course.student_set.remove(student)
	return redirect(reverse('student_find_by_course', kwargs={'id': course_id}))
