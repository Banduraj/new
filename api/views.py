from django.shortcuts import render
from loginapp.models import *
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import LoginSerializer,RegisterSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate 
from django.contrib.auth.hashers import make_password,check_password

@csrf_exempt
def loginview(request,*args,**kwargs):
   

    if request.method=='POST':
       data=JSONParser().parse(request)
       serializer=LoginSerializer(data=data, instance=data)
       if serializer.is_valid(raise_exception=True):
            username=serializer.data.get('username')
            password=serializer.data.get('password')
           
            user=Login.objects.filter(username=username)            
            if user:
                password=Login.objects.filter(password=password)
                if password:
                    return JsonResponse({'login':'success'})
                
                return JsonResponse('password doesnt match', safe= False)   
            return JsonResponse({'user not foun':'404 found'})
    return JsonResponse({'bad response'})
    
            
@csrf_exempt
def registerview(request,*args,**kwargs):
    if request.method=='POST':
        data=JSONParser().parse(request)
        serializer=RegisterSerializer(data=data)
        if serializer.is_valid():
            user=serializer.save()
            return JsonResponse({"register":"registersuccess"})
        else:
            return JsonResponse(serializer.errors)
    return JsonResponse({'bad request'})
            