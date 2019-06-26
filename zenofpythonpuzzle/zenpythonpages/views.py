from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "zenpythonpages/home.html")

def new_user(request):
    return render(request, "zenpythonpages/signup.html")

def profile(request):
    return render(request, "zenpythonpages/userprofile.html")

def submit_q(request):
    return render(request, "zenpythonpages/submitquestion.html")

def submit_comp(request):
    return render(request, "zenpythonpages/submitquestion.html")
