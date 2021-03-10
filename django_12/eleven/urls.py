from django.urls import path
from . import views

urlpatterns = [
	path('download/', views.download, name='eleven_download'),
	path('set_cookie/', views.set_cookie, name='eleven_set_cookie'),
	path('get_cookie/', views.get_cookie, name='eleven_get_cookie'),
	path('delete_cookie/', views.delete_cookie, name='eleven_delete_cookie'),
	path('page/<page>/', views.Page.as_view(), name='eleven_page'),
	path('login/', views.Login.as_view(), name='eleven_login'),
	path('register/', views.RegisterView.as_view(), name='eleven_register'),
]