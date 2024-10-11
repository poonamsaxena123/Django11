from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
 
    peoples =[
        {"name":"pooja","age":34},
        {"name":"prachi","age":21},
        {"name":"deepak","age":21},
        {"name":"nisha","age":31},
        {"name":"vishal","age":26}

    ]

    return render(request,"home/index.html",context={"peoples":peoples})

def about(request):
    return render(request,"home/about.html")

def contect(request):
    return render(request,"home/contect.html")