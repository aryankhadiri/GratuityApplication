from django.shortcuts import render, redirect
from .forms import LoginForm
from django.http import HttpResponse
from .models import User
from django.contrib.auth import authenticate, login


# Create your views here.
def login_view(request):
    error = ''
    form = LoginForm()
    
    if request.user.is_authenticated:
        
        # redirect the user based on their management status to their homepage
        if request.user.manager == True:
            return redirect('/manager/')
        else:
            #TODO 
            """User Homepage (no manager)"""
            
    if request.method == 'POST':
        if form.is_valid:
            
            useremail = request.POST.get('email')
            userpassword = request.POST.get('password')
            user = authenticate(request, email = useremail, password = userpassword)

            if user is not None:
                login(request, user)
                return redirect('/manager/')
            else:
                error = 'Incorrect Email/Password!'
                
        
  
    context = {
        'form':form,
        'error':error
    }
    
    return render(request,'login.html', context)
    