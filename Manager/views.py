from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from .form import EmployeeForm
from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required
def home_view(request):
    Hello = 'Hello Boys..Welcome!'
    context = {
        'Hello':Hello
    }
    return render(request, 'home.html', context)
#@login_required
#login_required is functional, just commented out for development process
def employee(request):
    form = EmployeeForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('employee')
    return render(request, 'pages/_index.html', {'form': form})
