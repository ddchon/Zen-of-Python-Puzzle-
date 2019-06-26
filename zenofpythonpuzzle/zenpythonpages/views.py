from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'zenpythonpages/home.html')

def new_user(request):
    return HttpResponse('This is the new user page.')
    
def profile(request):
    return HttpResponse('This is profile page.')

def submit_q(request):
    return HttpResponse('This is submit question page.')

def submit_comp(request):
    return HttpResponse('This is submit complete page.')

