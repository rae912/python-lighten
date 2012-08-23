# Create your views here.
#-*- coding:utf8 -*-
from django.shortcuts import render_to_response
from lighten.appuser.models import User
from forms import UserForm
import time
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import StringIO
import os
import Image
import re

def base(request):
    aa=request.session['name']
    k=User.objects.get(username=aa)
    return render_to_response('userbase.html',locals())
def usermodify(request):
    aa=request.session['name']
    no=User.objects.get(username=aa)
    if request.method=='POST':
    	pwd=request.POST.get('pwd','')
    	sex=request.POST.get('sex','')
    	mail=request.POST.get('mail','')
    	phone=request.POST.get('phone','')
    	image=request.POST.get('image','')
    	if pwd:
            pass
    	else:
            pwd=no.password
    	if sex:
    		pass
        else:
            sex=no.sex
    	if mail:
    		pass
        else:
            mail=no.email
    	if phone:
    		pass
        else:
            phone=no.phone
    	if image:
            image=no.avatar
        else:
            image=no.username+'.jpg'
        n1=User(username=no.username,password=pwd,sex=sex,email=mail,registrationtime=no.registrationtime,avatar=image,power=no.power,phone=phone)
        n1.save()
        #if 'file' in request.FILES:
        UPLOAD='./templates/images/header/'
        buf=request.FILES.get('image','')
        data=buf.read()
        f=StringIO.StringIO(data)
        image=Image.open(f)
        image=image.convert('RGB')
        name='%s%s' % (UPLOAD,no.username+'.jpg')
        image.thumbnail((250,250),Image.ANTIALIAS)
        image.save(file(name,'wb'),'PNG')
        
    	return base(request)
    return render_to_response('usermodify.html',locals())

def uadmin(request):
    form=UserForm()
    note=User.objects.all()
    return render_to_response('useradmin.html',locals())
def adduser(request):
    name=request.GET.get('username','')
    pwd=request.GET.get('passwd2','')
    powe=request.GET.get('power','')
    
    ISOTIMEFORMAT = "%Y-%m-%d"
    date = time.strftime(ISOTIMEFORMAT,time.localtime())
    s=User(username=name,password=pwd,registrationtime=date,power=powe,phone='00000000000')
    s.save()
    return uadmin(request)
def deluser(request,duser):
	s=User.objects.get(username=duser)
	s.delete()
	return uadmin(request)
	
	
