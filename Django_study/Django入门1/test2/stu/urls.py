#coding-utf-8

from django.urls import path
from . import views

urlpatterns = [
	path('index/', views.index_view),
	path('login/', views.login_view)
]
