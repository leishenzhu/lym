from django.db import models

# Create your models here.
class Student(models.Model):
	sname = models.CharField(max_length=30,unique=True)
	spwd = models.CharField(max_length=30)

	# 在admin后台展示使用
	def __unicode__(self):
		return u'Student:%s'%self.sname