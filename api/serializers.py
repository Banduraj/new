from rest_framework import serializers
from loginapp.models import *
from rest_framework.response import Response
from rest_framework import status




class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields=['id','username','password']

  




class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields='__all__'
    extra_kwargs={
        'username':{'required':True},
        'password':{'required':True}
    }
    def create(self, data):
        return Login.objects.create(**data)
    
        

