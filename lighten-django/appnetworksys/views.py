# coding:utf-8

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
import models
from lighten.appinfosys.models import hosts_info


def servicestatus(request):
    if request.method == 'POST':
	ipaddr = request.POST.get('ipaddr', '')
	try:	
	    conn = hosts_info.objects.get(ip=ipaddr)
	    macs = conn.mac
	    status = models.ServerStatus.objects.filter(mac=macs)
            return render_to_response('servicestatus.html', locals())
    	except:
	    status = {}
	    return render_to_response('servicestatus.html', locals())
    else:
	
        status = models.ServerStatus.objects.all()
        return render_to_response('servicestatus.html', locals())


def connect(request):
    
    if request.method == 'POST':
	ipaddr = request.POST.get('ipaddr', '')
	try:	
	    conn = hosts_info.objects.get(ip=ipaddr)
	    macs = conn.mac
	    connects = models.ServerStatus.objects.filter(mac=macs)
            return render_to_response('connect.html', locals())
    	except:
	    connects = {}
	    return render_to_response('connect.html', locals())
    else:
	connects = models.Connections.objects.all()    
	return render_to_response('connect.html', locals())
