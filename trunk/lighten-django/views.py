# Create your views here.
from django.shortcuts import render_to_response
from lighten.appuser.models import User
from django.http import HttpResponseRedirect

#def login(request):
#    return render_to_response('signin.html',locals())

def index(request):
    if request.method=='POST':
        uname = request.POST.get('userName','')
        passwd = request.POST.get('password','')
	try:
	    u = User.objects.get(username=uname)
	    if passwd == u.password:
		request.session['name'] = uname
		return render_to_response('middel.html',locals())
	    else:
		request.session['perror'] = "True"
		perror = "True"
		return render_to_response('signin.html',locals())
	except User.DoesNotExist:
	    request.session['uerror'] = "True"
	    uerror = "True"
	    return render_to_response('signin.html',locals())
    else:
	return render_to_response('signin.html',locals())

def quit(request):
    del request.session['name']
    return HttpResponseRedirect('/index/')
