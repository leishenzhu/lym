from django.urls import path
from . import views

urlpatterns = [
	path('custom_filter/', views.custom_filter),
]