from django.db import models

# Create your models here.
class Product(models.Model):
	name = models.TextField()
	price = models.FloatField()
	cover_map = models.TextField()
	link = models.TextField()
	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)
