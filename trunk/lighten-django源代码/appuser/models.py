from django.db import models
#-*- coding:utf-8 -*-

# Create your models here.

GENDER=(('M','男'),('F','女'),)
POWER=(('S','管理'),('P','普通'),)
class User(models.Model):
#    """
#    用户管理
#    #建立一个用户
#    >>>myuser=User.objects.create(username='sam',password='123456',sex='M',rphone='32165489715',power='S')
#    >>>myuser.cat()
#    'test data is :sma'
#    """
	username=models.CharField(max_length=20,primary_key=True)
	password=models.CharField(max_length=20)
	sex=models.CharField(max_length=4,choices=GENDER)
	email=models.EmailField()
	registrationtime=models.DateTimeField()
	phone=models.IntegerField(max_length=100)
	avatar=models.ImageField(upload_to='../templates/photo')
	power=models.CharField(max_length=4,choices=POWER)
	def __unicode__(self):
		return self.username

    
	
