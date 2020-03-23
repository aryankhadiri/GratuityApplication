"""GratuityProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
urlpatterns:  pa    2. Add a URL to th('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from django.urls import include
from .views import home_view
from . import views

urlpatterns = [
    path('homepage', home_view, name = 'home'),
    path('', home_view, name = 'home'),
    path('employee',views.employee, name='employee'),
]
