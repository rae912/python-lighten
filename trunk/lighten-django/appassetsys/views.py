# Create your views here.
#-*- coding:utf8 -*-
from django.shortcuts import render_to_response,get_object_or_404
from django.core.paginator import PageNotAnInteger,Paginator,InvalidPage,EmptyPage
from django.http import HttpResponseRedirect
from django.http import HttpResponse,Http404
from lighten.appassetsys.models import Hdinfo
from lighten.appassetsys.models import Blinfo
from forms import HdinfoForm
from forms import BlinfoForm
from django.core.urlresolvers import reverse
import datetime
from django.db.models import Q
from django.db.models import query
def  hardinfo(request):
    note = Hdinfo.objects.all() 
    after_range_num = 5     
    befor_range_num = 4 
    try:
        page = int(request.GET.get("page",1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    paginator = Paginator(note,5)  
    try:
        note = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        note = paginator.page(paginator.num_pages)
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
        page_range = paginator.page_range[0:int(page)+befor_range_num]
    return render_to_response('yjxx.html',locals())
def hdinfo(request):
    form = HdinfoForm()
    return render_to_response('yjxxadd.html',locals())
def uphdinfo(request,upsn):
    u1 = Hdinfo.objects.get(SerialNum = upsn)
    if request.method =='POST':
        form = HdinfoForm(request.POST, instance=u1)
        if form.is_valid():
            u1=form.save()
            return HttpResponseRedirect(reverse("assetsyshardinfo"))
    form = HdinfoForm(instance=u1)        
    return render_to_response('yjxxupdate.html',locals())
def hdinsert(request):
    if request.method == 'POST':
        form = HdinfoForm(request.POST)
        if form.is_valid():
            hd1 = request.POST.get('SerialNum','')
            hd2 = request.POST.get('ModelNum','')
            hd3 = request.POST.get('Cpu','')
            hd4 = request.POST.get('Memory','')
            hd5 = request.POST.get('MemNum','')
            hd6 = request.POST.get('Hdisk','')
            hd7 = request.POST.get('HdNum','')
            hd8 = request.POST.get('InternalNum','')
            hd9 = request.POST.get('DatePurchese','')
            try:
                tt = Hdinfo.objects.get(SerialNum = hd1)
                return HttpResponse("序列号重复")
            except:
                hd = Hdinfo(SerialNum=hd1,ModelNum=hd2,Cpu=hd3,Memory=hd4,MemNum=hd5,Hdisk=hd6,HdNum=hd7,InternalNum=hd8,DatePurchese=hd9)
                hd.save()
                return HttpResponseRedirect(reverse("assetsyshardinfo"))
    else:
        form = Hdinfo()
    return render_to_response('yjxxadd.html',locals())
def hdinfodel(request,delsn):
    d1 = Hdinfo.objects.get(SerialNum = delsn)
    d1.delete()
    return HttpResponseRedirect('/assetsys/hardinfo/')

def searchhdinfo(request):
    if 'q' in request.POST and request.POST['q']:
        q = request.POST['q']
        seasn = Hdinfo.objects.filter(ModelNum__icontains = q)
    else:
        seasn = Hdinfo.objects.order_by('SerialNum')

    after_range_num = 5     
    befor_range_num = 4 
    try:
        page = int(request.GET.get("page",1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    paginator = Paginator(seasn,5)  
    try:
        seasn = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        seasn = paginator.page(paginator.num_pages)
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
        page_range = paginator.page_range[0:int(page)+befor_range_num]
    return render_to_response('yjxxsearch.html',locals())


def beloneinfo(request):
    guishu = Blinfo.objects.all() 
    after_range_num = 5     
    befor_range_num = 4 
    try:
        page = int(request.GET.get("page",1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    paginator = Paginator(guishu,4)  
    try:
        guishu = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        guishu = paginator.page(paginator.num_pages)
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
        page_range = paginator.page_range[0:int(page)+befor_range_num]
    return render_to_response('fwqgsxx.html',locals())
def blinfo(request):
    belone = BlinfoForm()
    return render_to_response('fwqgsadd.html',locals())

def fwqgsinsert(request):
    if request.method == 'POST':
        belone = BlinfoForm(request.POST)
        if belone.is_valid():
            gs1 = request.POST.get('SerialNum','')
            print "guishu",gs1
            try:
                tt = Blinfo.objects.get(SerialNum = gs1)
                return HttpResponse("序列号重复")
            except:
                Blinfo=belone.save()
                return HttpResponseRedirect(reverse("assetsysbeloneinfo"))
    else:
        form = Blinfo()
    return render_to_response('fwqgsadd.html',locals())

def fwqgsup(request,gssn):
    g1 = Blinfo.objects.get(SerialNum = gssn)
    if request.method =='POST':
        form = BlinfoForm(request.POST, instance=g1)
        if form.is_valid():
            g1=form.save()
            return HttpResponseRedirect(reverse("assetsysbeloneinfo"))
    form = BlinfoForm(instance=g1)
    return render_to_response('fwqgsupdate.html',locals())

def fwqgsdel(request,gsdelsn):
    gd1 = Blinfo.objects.get(SerialNum = gsdelsn)
    gd1.delete()
    return HttpResponseRedirect('/assetsys/beloneinfo/')

def searchblinfo(request):
    if 'q' in request.POST and request.POST['q']:
        q = request.POST['q']
        gssn = Blinfo.objects.filter(SerialNum__icontains = q)
    else:
        gssn = Blinfo.objects.order_by('SerialNum')
    after_range_num = 5     
    befor_range_num = 4 
    try:
        page = int(request.GET.get("page",1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    paginator = Paginator(gssn,4)  
    try:
        gssn = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        gssn = paginator.page(paginator.num_pages)
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
        page_range = paginator.page_range[0:int(page)+befor_range_num]
    return render_to_response('fwqgssearch.html',locals())
