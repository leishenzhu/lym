from django.urls import path
from . import views

urlpatterns = [
	path('page/<page>/', views.page, name='ten_page'),
	path('httpRequestTest/', views.httpRequestTest, name='ten_http_test'),
	path('get_post/', views.get_post, name='ten_get_post'),
	path('user/', views.UserView.as_view(), name='ten_user'),
	path('upload/', views.Upload.as_view(), name='ten_upload'),
	path('student/', views.StudentView.as_view(), name='ten_student'),
]
