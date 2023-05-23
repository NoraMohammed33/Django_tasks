from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def viewlist(req):
    if (req.method == 'GET'):
        res = HttpResponse('Welcome to Noor')
        return res
    else:
        return HttpResponse('access denied')
def insert (req):
    return render(req,'student/insert.html')

def update(req):
    return render(req,'student/update.html')

def delete(req):
    return HttpResponseRedirect('/student/viewlist')