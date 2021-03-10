from django.urls import path
from . import views

urlpatterns = [
	path('test/', views.test),
	path('test1/', views.test1, name='test1'),
	# path('template_1/', views.template_1),
	path('template_2/', views.template_2),
	path('template_var/', views.template_var),
	path('index/<username>/<password>/',views.index),
]