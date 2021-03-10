from django.urls import path
from . import views

urlpatterns = [
	path('template_label/', views.template_label, name='template_label'),
	path('url_var/<var>', views.url_var, name='url_var'),
	path('index/<value>', views.index, name='index'),
]