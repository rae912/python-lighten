# Create your views here.
#-*- coding:utf-8 -*-

from django.shortcuts import render_to_response
from django.core.paginator import PageNotAnInteger,Paginator,InvalidPage,EmptyPage
import models

def index(request):
    name = request.GET.get('userName','')
    return render_to_response('middel.html',locals())

def hosts(request):
    #n1 = models.hosts_info_ip(ip='192.168.137.122',mac='00:FF:FG:WW:FC:33',idc='北京网通',infosys='Linux系统')
    #n1.save()
    if request.method=='POST':
        ipname = request.POST.get('ipname','')
	try:
	    host = models.hosts_info.objects.filter(ip=ipname)
	    return render_to_response('hosts.html',locals())
	except:
	    host = {}
	    return render_to_response('hosts.html',locals())
    else:
    	host = models.hosts_info.objects.all()

    after_range_num = 5         
    befor_range_num = 4 
    try:
        page = int(request.GET.get("page",1))
        if page < 1:
            page = 1 
    except ValueError:
        page = 1 
    paginator = Paginator(host,4)  
    try:
        host = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        host = paginator.page(paginator.num_pages)
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
        page_range = paginator.page_range[0:int(page)+befor_range_num]
        return render_to_response('hosts.html',locals())

def cpu(request):
    if request.method=='POST':
        ipname = request.POST.get('ipname','')
	try:
	    con = models.hosts_info.objects.get(ip=ipname)
	    cmac = con.mac
	    cpu = models.cpu_info.objects.filter(mac=cmac)
	    return render_to_response('cpu.html',locals())
	except:
	    cpu = {}
	    return render_to_response('cpu.html',locals())
    else:
    	cpu = models.cpu_info.objects.all()

    after_range_num = 5         
    befor_range_num = 4 
    try:
        page = int(request.GET.get("page",1))
        if page < 1:
            page = 1 
    except ValueError:
        page = 1 
    paginator = Paginator(cpu,4)  
    try:
        cpu = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        cpu = paginator.page(paginator.num_pages)
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
        page_range = paginator.page_range[0:int(page)+befor_range_num]
    	return render_to_response('cpu.html',locals())

def disk(request):
    if request.method=='POST':
        ipname = request.POST.get('ipname','')
	try:
	    con = models.hosts_info.objects.get(ip=ipname)
	    dmac = con.mac
	    disk = models.disk_info.objects.filter(mac=dmac)
	    return render_to_response('disk.html',locals())
	except:
	    disk = {}
	    return render_to_response('disk.html',locals())
    else:
    	disk = models.disk_info.objects.all()

    after_range_num = 5         
    befor_range_num = 4 
    try:
        page = int(request.GET.get("page",1))
        if page < 1:
            page = 1 
    except ValueError:
        page = 1 
    paginator = Paginator(disk,8)  
    try:
        disk = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        disk = paginator.page(paginator.num_pages)
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
        page_range = paginator.page_range[0:int(page)+befor_range_num]
    	return render_to_response('disk.html',locals())

def network(request):
    if request.method=='POST':
        ipname = request.POST.get('ipname','')
	try:
	    con = models.hosts_info.objects.get(ip=ipname)
	    nmac = con.mac
	    network = models.network_info.objects.filter(mac=nmac)
	    return render_to_response('network.html',locals())
	except:
	    network = {}
	    return render_to_response('network.html',locals())
    else:
    	network = models.network_info.objects.all()
    after_range_num = 5         
    befor_range_num = 4 
    try:
        page = int(request.GET.get("page",1))
        if page < 1:
            page = 1 
    except ValueError:
        page = 1 
    paginator = Paginator(network,4)  
    try:
        network = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        network = paginator.page(paginator.num_pages)
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
        page_range = paginator.page_range[0:int(page)+befor_range_num]
    	return render_to_response('network.html',locals())

def ipnet(request):
    if request.method=='POST':
        ipname = request.POST.get('ipname','')
	try:
	    ipnet = models.ipnet_info.objects.filter(ipnet=ipname)
	    return render_to_response('ipnet.html',locals())
	except:
	    ipnet = {}
	    return render_to_response('ipnet.html',locals())
    else:
    	ipnet = models.ipnet_info.objects.all()
    after_range_num = 5         
    befor_range_num = 4 
    try:
        page = int(request.GET.get("page",1))
        if page < 1:
            page = 1 
    except ValueError:
        page = 1 
    paginator = Paginator(ipnet,4)  
    try:
        ipnet = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        ipnet = paginator.page(paginator.num_pages)
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
        page_range = paginator.page_range[0:int(page)+befor_range_num]
    	return render_to_response('ipnet.html',locals())

def ipadd(request):
    if request.method=='GET':
	ip = request.GET.get('ipnet','')
	name = request.GET.get('netname','')
	try:
	    add = models.ipnet_info(ipnet=ip,netname=name)
	    add.save()
    	    ipnet = models.ipnet_info.objects.all()
	    return render_to_response('ipnet.html',locals())
	except:
    	    ipnet = models.ipnet_info.objects.all()
	    return render_to_response('ipnet.html',locals())
