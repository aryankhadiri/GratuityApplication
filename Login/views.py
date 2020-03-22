"""
This file contains a function-based view for the Login page.
"""

# -----------------------------------------------------------------------------------------------------------------------------------------
#       IMPORTS                 
# -----------------------------------------------------------------------------------------------------------------------------------------
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.http import HttpResponse
from .models import User
from django.contrib.auth import authenticate, login

# -----------------------------------------------------------------------------------------------------------------------------------------
#       LOGIN             
# -----------------------------------------------------------------------------------------------------------------------------------------
def login_view(request):

    error = ''
    form = LoginForm()
<<<<<<< HEAD
    
=======

>>>>>>> d805aaa4d7f0580139dd0bbbc408b03022906e35
    if request.user.is_authenticated:
        # redirect the user (based on their management status) to their appropriate homepage
        if request.user.manager == True:
            return redirect('/manager/')
<<<<<<< HEAD
        else:
            #TODO 
            """User Homepage (no manager)"""
            
=======

>>>>>>> d805aaa4d7f0580139dd0bbbc408b03022906e35
    if request.method == 'POST':
        if form.is_valid:
            user_email = request.POST.get('email')
            user_password = request.POST.get('password')
            user = authenticate(request, email = user_email, password = user_password)

            if user is not None:
                login(request, user)
                return redirect('/manager/')
            else:
                error = 'Incorrect email/password combination.'
        
    context = {
        'form':form,
        'error':error
    }
    
    return render(request,'login.html', context)
# -----------------------------------------------------------------------------------------------------------------------------------------
    