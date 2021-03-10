from django.db import models


# Create your models here.
# 模型类 --> 需要继承models模板中的Model类
# 
class User(models.Model):
	# 映射方法
	# django会自动加id，可以省略
	# id = models.AutoField(primary_key=True)  # int 主键 自增
	name = models.CharField(max_length=30)  # varchar
	age = models.IntegerField(null=True)
	sex = models.IntegerField(null=True)
	city = models.CharField(max_length=30, null=True)
	note = models.TextField(null=True)
	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return 'id=%s,name=%s,age=%s,city=%s,note=%s' % (self.id, self.name, self.age, self.city, self.note)
