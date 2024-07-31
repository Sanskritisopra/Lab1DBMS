from django.shortcuts import render
from django.http import HttpResponse
from .models import XYZCompany
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.

def home(request):
    peoples = [
        {'name':'xyz','age':26},
        {'name':'abc','age':23},
        {'name':'def','age':24}
    ]
    return render(request,"index.html",context={'peoples':peoples})

def success_page(request):
    return HttpResponse("Hello")

def allinterns(request):
    interns = XYZCompany.objects.all()
    
    return render(request,'index.html',{'interns':interns})


# @login_required
# def search_intern(request):
    