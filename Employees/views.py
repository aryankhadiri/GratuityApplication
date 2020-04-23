from django.shortcuts import render, redirect
from .forms import newForm, TipForm
from .models import Employee, Tip, Form
from datetime import datetime
from django.forms import modelformset_factory, formset_factory
import json
from django.contrib import messages
from django.template import RequestContext


# Create your views here.
def home_view(request):
    title = 'Dashboard | Employee'
    js_dict = sendEmployeeDataAsJSON()
    form = formset_factory(TipForm)
    if request.method == 'POST':
        form1 = form(request.POST)
        new_form= newForm(request.POST)
        if form1.is_valid() and form1.has_changed():   
            for f in form1:
                print(f)
                new_instance = f.save(commit=False)
                new_instance.date = request.POST.get('date')
                new_instance.time_frame = request.POST.get('time_frame')
                new_instance.save()
                
            messages.success(request, "The Tips have been successfully saved!")

        else:
            messages.error(request, form1.errors)
            return render(request, 'employee_home.html', {'form':form1, 'new_form':new_form,
            'js_dict':js_dict})
        
        if new_form.is_valid():
            new_instance2 = new_form.save(commit = False)
            new_instance2.time = datetime.now().time()
            new_instance2.save()
            messages.success(request, "The form has been successfully saved!")
        else:
            messages.error(request, new_form.errors)
            return render(request, 'employee_home.html',{'form':form1, 'new_form':new_form,
            'js_dict':js_dict})
            
            
        
    new_form = newForm()

    #form = tip_form_set(queryset = Tip.objects.none())
    print(form)
    context = {
        'title': title,
        'new_form':new_form,
        'js_dict':js_dict,
        'form':form
    }
    return render(request, 'employee_home.html', context)

        #tip_form = TipForm(request.POST, prefix="form1")
        #new_form = newForm(request.POST, prefix="form2")
        #if new_form.is_valid():
         
            #new_form.save()
            #tip_form.save()
            

    #tip_form = TipForm(prefix="form1")
    #new_form = newForm(prefix="form2")
    """ date = request.POST.get('date')
        tip_amount = request.POST.get('tip_amount')
        time_frame = request.POST.get('time_frame')
        paid_later = request.POST.get('paid_later')
        point = request.POST.get('point')
        employee = request.POST.get('employee')
        e = Tip(date = date, tim_amount = tip_amount, time_frame = time_frame, paid_later = paid_later
        ,point = point, employee = employee)
        e.save()"""
def sendEmployeeDataAsJSON():
    query = Employee.objects.all()
    dict = {}
    for emp in query:
        dict[emp.id] = emp.point
    js_dict = json.dumps(dict)
    return js_dict