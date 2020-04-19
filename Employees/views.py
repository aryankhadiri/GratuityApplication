from django.shortcuts import render
from .forms import newForm, TipForm
from .models import Employee, Tip, Form
from datetime import datetime
# Create your views here.
def home_view(request):
    """ date = request.POST.get('date')
        tip_amount = request.POST.get('tip_amount')
        time_frame = request.POST.get('time_frame')
        paid_later = request.POST.get('paid_later')
        point = request.POST.get('point')
        employee = request.POST.get('employee')
        e = Tip(date = date, tim_amount = tip_amount, time_frame = time_frame, paid_later = paid_later
        ,point = point, employee = employee)
        e.save()"""
    query = Employee.objects.all()
    if request.method == 'POST':
    
        tip_form = TipForm(request.POST, prefix="form1")
        new_form = newForm(request.POST, prefix="form2")
        
        if new_form.is_valid():
         
            new_form.save()
            tip_form.save()
            

    tip_form = TipForm(prefix="form1")
    new_form = newForm(prefix="form2")

    
    context = {
        'new_form':new_form,
        'tip_form':tip_form,
        'list':query,
    }
    return render(request, 'employee_home.html', context)
