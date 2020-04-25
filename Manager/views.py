from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Employee
from Employees.models import Tip, Form
from django.contrib import messages
from .form import EmployeeForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from datetime import timedelta
from django.contrib.auth import logout
from datetime import datetime, timedelta


# Create your views here.
#@login_required

def home_view(request):
    if request.user.manager == False:
        return redirect('/employee/')
    title = 'Manager / Home'
    page = 'Home'
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
        "page": page,
        'allForms':allForms
    }
    return render(request, 'home.html', context)
#@login_required
#login_required is functional, just commented out for development process
def add_employee_view(request):
    if request.user.manager == False:
        return redirect('/employee/')
    title = 'Manager / Add Employee'
    page = 'Add Employee'
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
            'page': page,
            'form': form
        }
        return render(request, 'employee.html', context)
    
    form = EmployeeForm()
    context = {
        'title': title,
        'page': page,
        'form': form
    }
    return render(request, 'employee.html', context)
    
def list_employee_view(request):
    if request.user.manager == False:
        return redirect('/employee/')
    title = 'Manager / Edit Employee'
    page = "Edit Employee"
    queryset = Employee.objects.all()
    context = {
        "list": queryset,
        "title": title,
        "page": page
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

    if request.method == 'POST':
        print(request.POST)
        today_date_str = request.POST['date_input']
        today_date = datetime.strptime(today_date_str, '%Y-%m-%d').date()

        today_day = today_date.weekday()
    else:
        today_day = datetime.today().weekday()
        today_date = datetime.today().date()

    #print(today_date)
    
    first_date_of_week = today_date - timedelta(today_day)
    last_date_of_week = first_date_of_week + timedelta(7)
    days_dates=[]
    for i in range(0,7):
        days_dates.append(first_date_of_week+timedelta(i))

    tips = Tip.objects.filter(date__lte = last_date_of_week).filter(date__gte=first_date_of_week).order_by('date')
    employees = Employee.objects.all().order_by('name')
    
    all_info = {}
    total_info = {}
    for employee in employees:
        all_info[employee.name] = {}
        total_info[employee.name] = 0
        for day in days_dates:
            all_info[employee.name][day]=['','']
    for tip in tips:
        if tip.time_frame == 'AM':
            all_info[tip.employee.name][tip.date][0] = tip.paid_later
            total_info[tip.employee.name] += tip.paid_later
        else:
            all_info[tip.employee.name][tip.date][1] = tip.paid_later
            total_info[tip.employee.name] += tip.paid_later
    print(total_info)
    for tip in tips:
        print(tip.employee.name , "  ", tip.date , tip.time_frame, tip.paid_later, tip.paid_today)
#    print(all_info)


    """all_info = {}
    for employee in employees:
        all_info[employee.name] = []
        for tip in tips:
            if tip.employee == employee:
                all_info[employee.name].append({tip.date:[{tip.time_frame:tip.paid_later}]})
    for key in all_info:
        for i in range(0, 7):"""
            

                
    
    context = {
        'title':title,
        'tips':tips,
        'employees':employees,
        'days_dates':days_dates,
        'all_info':all_info,
        'total_info': total_info
    }
    
    return render(request, 'weekly_reports.html', context)
    
def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect ('login')
