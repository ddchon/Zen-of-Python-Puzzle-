from django.shortcuts import render
from django.http import HttpResponse

def q_home(request):
    return HttpResponse('This is questions homepage.')

def ind_questions(request):
    return HttpResponse('This is individual questions page.')

def q_success(request):
    return HttpResponse('This is success questions page.')

def q_fail(request):
    return HttpResponse('This is fail questions page.')

