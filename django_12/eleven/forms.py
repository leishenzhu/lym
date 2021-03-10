from django import forms


class RegisterForm(forms.Form):
	username = forms.CharField(max_length=30, min_length=6, widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	password = forms.CharField(max_length=100, min_length=6, widget=forms.PasswordInput(attrs={'placeholder': '请输入密码'}))
	password_repeat = forms.CharField(max_length=100, min_length=6,
									  widget=forms.PasswordInput(attrs={'placeholder': '请确认密码'}))

	email = forms.EmailField()
