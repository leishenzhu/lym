# 自定义上下文处理器，必须返回字典类型，所有模板都能调用
def my_user(request):
	username = request.session.get('username', None)
	print('上下文处理器')
	return {'username': username}
