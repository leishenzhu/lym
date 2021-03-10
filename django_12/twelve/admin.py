from django.contrib import admin
from nine.models import Student, StudentDetails, Classes, Course


# Register your models here.
class ClassesAdmin(admin.ModelAdmin):
	# 列表页属性
	list_display = ['id', 'name', 'slogan']  # 通过表格显示字段，可以排序
	list_filter = ['slogan']  # 过滤字段
	search_fields = ['name']  # 搜索字段,可以模糊查询
	list_per_page = 2  # 进行分页，几条数据为一页
	list_display_links = ['id', 'name', 'slogan']  # 字段为连接，点击可以修改
	# 修改页属性
	fields = ['slogan','name']
	# fieldsets = [('一组', {'fields': ['slogan']}), ('二组', {'fields': ['name']})]  # 升级版


admin.site.register(Student)
admin.site.register(StudentDetails)
admin.site.register(Classes, ClassesAdmin)
admin.site.register(Course)
