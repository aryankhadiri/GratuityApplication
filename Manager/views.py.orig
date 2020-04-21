from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from .form import EmployeeForm
from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required

def home_view(request):
<<<<<<< HEAD
    if request.user.manager == False:
        return redirect('/employee/')
    Hello = 'Hello Boys..Welcome!'
=======
    title = 'Dashboard | Home'
>>>>>>> master
    context = {
        'title': title
    }
    return render(request, 'home.html', context)
#@login_required
#login_required is functional, just commented out for development process
def add_employee_view(request):
<<<<<<< HEAD
    if request.user.manager == False:
        return redirect('/employee/')
    title = 'Adding Employee'
=======
    title = 'Dashboard | Add Employee'
>>>>>>> master
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if request.POST.get('cancel_button') == '':
            return redirect('home')
        if form.is_valid():
             
            name = request.POST['name']
            if Employee.objects.filter(name=name).exists():
                messages.error(request, 'Employee was already Added')
                return redirect('add_employee')
            else:   
                form.save()
                messages.success(request, 'Employee Successfully Added')
                return redirect('add_employee')
        else:
            messages.error(request, 'The form is invalid.')
            return redirect('add_employee')


        context = {
            'title': title,
            'form': form
        }
        return render(request, 'employee.html', context)
    
    form = EmployeeForm()
    context = {
        'form':form,
        'title':title
    }
    return render(request, 'employee.html', context)
    
def list_employee_view(request):
    if request.user.manager == False:
        return redirect('/employee/')
    queryset = Employee.objects.all()
    context = {
        "list":queryset
    }
    return render (request,'list.html', context)

def update_employee_view(request, id=id):
    if request.user.manager == False:
        return redirect('/employee/')
    title = 'Update Employee Information'
    employee = get_object_or_404(Employee, id=id)
    form = EmployeeForm(request.POST or None, instance = employee)
    if request.POST.get('cancel_button') == '':
        return redirect('list_employee')
    if form.is_valid():
        if request.POST.get('save_button') == '':
            form.save()
            return redirect('list_employee')
        
        elif request.POST.get('delete_button') == '':
            employee.delete()
            return redirect('list_employee')

    context = {
        'form':form,
        'title':title
    }
    return render(request,'employee.html', context)
    
