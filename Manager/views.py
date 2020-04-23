from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Employee
from Employees.models import Tip, Form
from django.contrib import messages
from .form import EmployeeForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from datetime import timedelta

# Create your views here.
#@login_required

def home_view(request):
    if request.user.manager == False:
        return redirect('/employee/')
    title = 'Dashboard | Home'

    if request.method == 'POST':
        start_date = request.POST['start_date_input']
        end_date = request.POST['end_date_input']
        forms = Form.objects.filter(date__gte=start_date).filter(date__lte=end_date)
        return render(request, 'home.html', {'allForms':forms})
    
    today_date = datetime.today().date()
    week_ago = today_date - timedelta(days=7)
    allForms = Form.objects.filter(date__gte = week_ago)
    #fetch all the forms submitted between week ago and today. 
    context = {
        'title': title,
        'allForms':allForms
    }
    return render(request, 'home.html', context)
#@login_required
#login_required is functional, just commented out for development process
def add_employee_view(request):
    if request.user.manager == False:
        return redirect('/employee/')
    title = 'Adding Employee'
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
    
def weekly_report_view(request):
    title = "Weekly Reports"




    today_day = datetime.today().weekday()
    today_date = datetime.today().date()
    first_date_of_week = today_date - timedelta(today_day)
    last_date_of_week = first_date_of_week + timedelta(7)
    days_dates=[]
    for i in range(0,7):
        days_dates.append(first_date_of_week+timedelta(i))

    tips = Tip.objects.filter(date__lte = last_date_of_week).filter(date__gte=first_date_of_week).order_by('employee__name')
    employees = Employee.objects.all().order_by('name')
    
                
    
    context = {
        'title':title,
        'tips':tips,
        'employees':employees,
        'days_dates':days_dates
    }
    for tip in tips:
        print(tip.employee)
    return render(request, 'weekly_reports.html', context)