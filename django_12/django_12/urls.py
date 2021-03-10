"""django_12 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from . import views

# path: 第一个参数：资源地址；第二个参数：调用函数
"""
    转换器：
        str,int,slug,uuid,path
"""
urlpatterns = [
	path('admin/', admin.site.urls),
	path('test/', views.test),
	path('course/<str:name>', views.course),
	# (?P<参数名>正则规则)
	re_path('^testRepath/(?P<var>[0-9]+)/$', views.testRepath),
	# APP路由注册 使用include函数 ，第二个参数为APP的路由文件
	path('two/', include('two.urls')),
	path('three/', include('three.urls'), {'time': True}),	# 字典数据 会传递这个参数给app下的所有视图函数
	path('four/', include('four.urls')),
	path('five/', include('five.urls')),
	path('six/', include('six.urls')),
	path('seven/', include('seven.urls')),
	path('eight/', include('eight.urls')),
	path('nine/', include('nine.urls')),
	path('ten/', include('ten.urls')),
	path('eleven/', include('eleven.urls')),
	path('twelve/', include('twelve.urls')),
]
