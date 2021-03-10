from django.urls import path
from . import views

urlpatterns = [
	path('page/<index>/', views.page, name='page'),
	path('classes_add/', views.classes_add, name='classes_add'),
	path('student_add/', views.student_add, name='student_add'),
	path('course_add/', views.course_add, name='course_add'),
	path('classes_del/<id>/', views.classes_del, name='classes_del'),
	path('student_del/<id>/', views.student_del, name='student_del'),
	path('course_del/<id>/', views.course_del, name='course_del'),
	path('classes_update/<id>/', views.classes_update, name='classes_update'),
	path('student_update/<id>/', views.student_update, name='student_update'),
	path('course_update/<id>/', views.course_update, name='course_update'),
	path('cstudent/<id>/', views.student_find_by_classes, name='student_find_by_classes'),
	path('costudent/<id>/', views.student_find_by_course, name='student_find_by_course'),
	path('costudent_add/<id>/', views.student_add_by_course, name='student_add_by_course'),
	path('course_add_student/', views.course_add_student, name='course_add_student'),
	path('course_del_student/<course_id>/<student_id>/', views.course_del_student, name='course_del_student'),
]
