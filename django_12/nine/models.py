from django.db import models


# Create your models here.
class Classes(models.Model):
	name = models.CharField(max_length=30)
	slogan = models.TextField(null=True)
	create_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return 'id=%s,name=%s,slogan=%s' % (self.id, self.name, self.slogan)


class Course(models.Model):
	name = models.CharField(max_length=30)
	credit = models.FloatField(default=0.0, blank=True)
	duration = models.FloatField(default=2.0, blank=True)

	def __str__(self):
		return 'id=%s,name=%s,credit=%s,duration=%s' % (self.id, self.name, self.credit, self.duration)


class Student(models.Model):
	name = models.CharField(max_length=30)
	credit = models.FloatField(default=0.0)
	create_time = models.DateTimeField(auto_now_add=True)
	classes = models.ForeignKey('Classes', on_delete=models.PROTECT)
	course = models.ManyToManyField('Course')  # django会自动创建中间表，建立外键，关联两张表的主键，设置为联合主键

	def __str__(self):
		return 'id=%s,name=%s,credit=%s,create_time=%s,classes=%s,course=%s' % (
			self.id, self.name, self.credit, self.create_time, self.classes, self.course)


class StudentDetails(models.Model):
	age = models.IntegerField(null=True, blank=True)
	sex = models.IntegerField(null=True, blank=True)
	city = models.CharField(max_length=30, null=True, blank=True)
	note = models.TextField(null=True, blank=True)
	update_time = models.DateTimeField(auto_now=True)
	student = models.OneToOneField('Student', on_delete=models.CASCADE)

	def __str__(self):
		return 'id=%s,age=%s,sex=%s,city=%s,note=%s,update_time=%s,student=%s' % (
			self.id, self.age, self.sex, self.city, self.note, self.update_time, self.student)
