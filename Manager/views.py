from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request):
    Hello = 'Hello Boys..Welcome!'
    context = {
        'Hello':Hello
    }
    return render(request, 'home.html', context)
