from django.urls import path
from . import views

urlpatterns = [
	path('test/', views.test, name='twelve_test'),
	path('test1/', views.test1, name='twelve_test1'),
]
