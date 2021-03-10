from django.urls import path
from . import views

urlpatterns = [
	path('find/', views.find),
	path('product/<page>/', views.product, name='product'),
	path('product_add/', views.product_add, name='product_add'),
]
