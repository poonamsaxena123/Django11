from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate ,login

# Create your views here.
def receipe(request):
   if request.method == "POST":
      data = request.POST 

      image = request.FILES.get("receipe_image")
      receipe_name = data.get("name")
      description = data.get("description")
      # rating = data.get("rating")  

      Receipe.objects.create(
        receipe_image=image,
        name=receipe_name,
        description=description,
      #   rating=rating,  
      )
      return redirect("/receipes/")
   
   queryset = Receipe.objects.all()
   context = {"receipe": queryset}

   return render(request, 'receipes.html', context)

  

def delete_receipe(request,id):
   queryset = Receipe.objects.get(id=id)
   queryset.delete()
   return redirect("/receipes/")

 


def update_receipe(request,id):
   queryset=Receipe.objects.get(id=id)
   if request.method == "POST":
      data = request.POST

      image =request.FILES.get("receipe_image")
      receipe_name =data.get("name")
      description =data.get("description")
      
      queryset.receipe_name=receipe_name
      queryset.description =description

      if image :
         queryset.image=image


      queryset.save()
      return redirect("/receipes/")


   context ={"receipe":queryset}

   return render(request,'update_receipe.html',context)



def login_page(request):
   if request.method=='POST':
         username =request.POST.get('username')
         password =request.POST.get('password')
         
         if not User.objects.filter(username=username).exists():
            messages.error(request, "invalide username")
            return redirect('/login/')
         user =authenticate(username=username,password=password)
         
         if user is None:
            messages.error(request, "invalid password")
            return redirect('/login/')
         else :
            login(user)
            return redirect('/reciepes/')
   return render(request,"login.html")

def register_page(request):
   if request.method=='POST':
      first_name =request.POST.get('first_name')      
      last_name =request.POST.get('last_name')
      username =request.POST.get('username')
      password =request.POST.get('password')

      user =User.objects.filter(username=username)

      if user.exists():
         return redirect('/register/')

      user =User.objects.create(
         first_name  =first_name,
         last_name=last_name,
         username=username,

      )
      user.set_password(password)
      user.save()

      return redirect('/register/')
   return render(request,"register.html")