from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dict = {'include_me':'first page'}
    return render(request,'AppTwo/index.html',context = my_dict)

def help(request):
    my_dict = {'include_me':'second page'}
    return render(request,'AppTwo/help.html',context=my_dict)
# Create your views here.
