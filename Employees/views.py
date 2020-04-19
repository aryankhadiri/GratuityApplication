from django.shortcuts import render
from .forms import newForm, TipForm
from .models import Employee, Tip, Form
from datetime import datetime
from django.forms import modelformset_factory
# Create your views here.
def home_view(request):
    
    query = Employee.objects.all()
    tip_form_set = modelformset_factory(Tip, exclude=('date',))

    if request.method == 'POST':
        print(request.POST)
        form1 = tip_form_set(request.POST)

        for f in form1:
            if f.is_valid():
                new_instance = f.save(commit=False)
                new_instance.date = request.POST.get('date')
                new_instance.time_frame = request.POST.get('time_frame')
                new_instance.save()
            else:
                print(f.errors)
        new_form= newForm(request.POST)
        print(new_form)
        if new_form.is_valid():
            new_instance2 = new_form.save(commit = False)
            new_instance2.time = datetime.now().time()
            new_instance2.save()
        else:
            print(new_form.errors)
            
            
        
        
    new_form = newForm()
    form = tip_form_set(queryset = Tip.objects.none())
    
    context = {
        'new_form':new_form,
        'list':query,
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