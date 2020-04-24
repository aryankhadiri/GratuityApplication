from django.contrib import admin
from django.urls import path
from .views import *
from django.urls import include
from .views import home_view
from . import views

urlpatterns = [
    path('homepage', home_view, name = 'home'), 
    path('', home_view, name = 'home'),
     path('logout', logout_employee,name = 'logoutEmployee'),  
]
