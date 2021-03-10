from django.urls import path
from . import views

urlpatterns = [
	path('filter_var/', views.filter_var),
	path('static_file/', views.static_file),
	path('template_label/',views.template_label)
]