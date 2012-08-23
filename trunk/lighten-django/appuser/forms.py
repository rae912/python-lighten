#-*- coding:utf-8 -*-
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError 
from lighten.appuser.models import User

POWER=(('P','普通'),('S','管理'),)
class UserForm(forms.Form):
	username=forms.CharField(label='用户名',max_length=20)
	password1=forms.CharField(label='密码',max_length=20,widget=forms.PasswordInput())
	password2=forms.CharField(label='确认密码',max_length=20,widget=forms.PasswordInput())
	power=forms.ChoiceField(label='权限',choices=POWER)
	def clean_username(self):
		username=self.cleaned_data['username']
		num_words=len(username)
		if num_words<3:
			raise forms.ValidationError("用户名小于3！")
		try:
			User.objects.get(username=username)
		except ObjectDoesNotExist:
			return username

		raise forms.ValidationError("用户名已存在！")

	def clean_password2(self):
            if 'password1' in self.cleaned_data:
                password1=self.cleaned_data['password1']
                password2=self.cleaned_data['password2']
                if password1==password2:
                    pass
                else:
                    raise forms.ValidationError('两次密码不一样!')

