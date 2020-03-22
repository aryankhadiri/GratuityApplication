from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request):
    Hello = 'Hello Boys..Welcome!'
    context = {
        'Hello':Hello
    }
    return render(request, 'home.html', context)

def employee(request):
    if request.method == 'POST':
        name = request.POST['name']
        point = request.POST['point']
        phone = request.POST['phone']
        if Employee.objects.filter(name=name).exists():
            messages.error(request,'This Employess is already added')
            return redirect ('employee')
        else:  
            employee = Employee.objects.create(name=name, point=point, phone=phone)
            employee.save()
       #    print (employee)
            messages.success(request,'Employee succesfully added')
            return redirect ('employee')
    return render (request, 'pages/_index.html')
