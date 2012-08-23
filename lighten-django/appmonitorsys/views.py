# Create your views here.
#-*- coding:utf8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse 
from models import *
from lighten.appinfosys.models import hosts_info
import time


def maping(request):
    if request.method=='GET':
	mmac = request.GET.get('mac','')
	date = request.GET.get('strtime','')
	enddate = request.GET.get('endtime','')
	if not date:
   	    date = time.strftime("%Y-%m-%d")
	if not enddate:
    	    enddate = time.strftime("%Y-%m-%d %H:%M:%S")
    	ip = hosts_info.objects.get(mac=mmac)
    	Test = DataHandle(mmac,date,enddate)
    	flow,package,inflow,outflow,inpack,outpack = Test.SelectNetwork()
    	load,use = Test.SelectCpu()
    	mem = Test.SelectMem()
    	count = Test.SelectCount()
    	return render_to_response('m1.html', locals())
    else:
	return render_to_response('state.html', locals())

def netstate(request):
    state = serverstate.objects.all()
    return render_to_response('state.html', locals())
    
