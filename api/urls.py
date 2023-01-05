from django.urls import path
from .views import loginview,registerview




urlpatterns = [
   path('login/',loginview ),
   path('register/',registerview ),

]