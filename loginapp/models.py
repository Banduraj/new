from django.db import models


# Create your models here.
class Login(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField()
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
   
   
   



    
