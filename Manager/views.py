from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Employee
from Employees.models import Tip, Form
from django.contrib import messages
from .form import EmployeeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
#@login_required

def home_view(request):
    if request.user.manager == False:
        return redirect('/employee/')
    title = 'Dashboard | Home'
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
        'allForms':allForms
    return render(request, 'home.html', context)
#@login_required
#login_required is functional, just commented out for development process
def add_employee_view(request):
    if request.user.manager == False:
        return redirect('/employee/')
    title = 'Adding Employee'
    title = 'Dashboard | Add Employee'
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
    title = 'Dashboard | Edit Employee'
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
    
def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect ('login')
