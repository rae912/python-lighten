# Create your views here.
from django.shortcuts import render_to_response

def serverlog(request):
    return render_to_response('serverlog.html',locals())
def loginlog(request):
    return render_to_response('loginlog.html',locals())
def faultlog(request):
    return render_to_response('faultlog.html',locals())
