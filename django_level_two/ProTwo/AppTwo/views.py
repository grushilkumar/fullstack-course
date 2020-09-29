from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

def index(request):
    names_list = User.objects.order_by('firstname')
    name_dict = {'names_records':names_list}
    return render(request,'AppTwo/index.html',context = name_dict)

def help(request):
    my_dict = {'include_me':'second page'}
    return render(request,'AppTwo/help.html',context=my_dict)
# Create your views here.
