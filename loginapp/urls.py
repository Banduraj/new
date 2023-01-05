
from django.urls import path
from .views import home,signin,signout,signup

urlpatterns = [
    path('home',home,name='home'),
    path('signin',signin,name='signin'),
    path('signout', signout,name='signout'),
    path('signup',signup,name='signup'),
    
]
