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
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid(): 
            name = request.POST['name']
            if Employee.objects.filter(name=name).exists():
                messages.error(request, 'Employee was already Added')
                return redirect('employee')
            else:   
                form.save()
                messages.success(request, 'Employee Successfully Added')
                return redirect('employee')
        else:
            messages.error(request, 'The form is invalid.')

        return render(request, 'pages/_index.html', {'form': form})
    else:
        form = EmployeeForm()
        return render(request, 'pages/_index.html', {'form': form})
    
def listEmployee(request):
    queryset = Employee.objects.all()
    context = {
        "list":queryset
    }
    return render (request,'pages/list.html', context)
