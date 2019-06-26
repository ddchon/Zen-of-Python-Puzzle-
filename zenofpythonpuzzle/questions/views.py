from django.shortcuts import render
from django.http import HttpResponse

def q_home(request):
    return render(request, "questions/questionshome.html")

def ind_questions(request):
    return render(request, "questions/ind_question.html")

def q_success(request):
    return render(request, "questions/q_success.html")

def q_fail(request):
    return render(request, "questions/q_fail.html")
