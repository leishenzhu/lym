from django.urls import path
from . import views

urlpatterns = [
	path('user_add/', views.user_add),
	path('user_find/', views.user_find),
	path('user_update/', views.user_update),
	path('user_del/', views.user_del),
]