from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def dateTime(request):
    date=datetime.datetime.now()
    x=int(date.strftime('%H'))
    msg='<h1>Hello sarath very '
    if(x<12):
        msg=msg+'Goood morning'
    elif(x<16):
        msg=msg+'Good afternoon'
    elif(x<19):
        msg=msg+'Good evening'
    else:
        msg=msg+'Good night'

    msg=msg+'</h1><hr>'
    msg=msg+'<h1>The system date and time is:'+str(date)+'</h1>'

    return HttpResponse(msg)
