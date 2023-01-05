from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Login
from django.contrib import messages

def home(request):
    return render(request,'home.html') 
  


def signup(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        username=request.POST.get('username')
        password=request.POST.get('password')
       
        email=request.POST.get('email')

        object=Login.objects.create()
        object.firstname=firstname
        object.lastname=lastname
        object.username=username
        object.password=password
        object.email=email
        object.save()
        messages.success(request,'object created successfully')
        return redirect('signin')
    else:
        return render(request, 'signup.html')
   

def signin(request):
    if request.method=='POST':
         username=request.POST.get('username')
         password=request.POST.get('password')
         error_msg=''
         match=Login.objects.filter(password=password,username=username)
         if match:
           return redirect('home')
         error_msg='username and password doesnt match'
         return render(request,'signin.html',{'error_msg': error_msg})
        
    return render(request,'signin.html')

def signout(request):
    request.session.clear()
    msg='successfully logout'
    return render(request,'home.html',{'msg':msg})