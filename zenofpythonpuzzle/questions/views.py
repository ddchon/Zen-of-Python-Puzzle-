from django.shortcuts import render, redirect
from .models import Question

def q_home(request):
    return render(request, "questions/questionshome.html")

def ind_questions(request):
    return render(request, "questions/ind_question.html")

def new_question(request):
    if request.method == "POST":
        new_question = Question (question=request.POST["question"],
                                 p_answer1=request.POST["p_answer1"],
                                 p_answer2=request.POST["p_answer2"],
                                 p_answer3=request.POST["p_answer3"],
                                 p_answer4=request.POST["p_answer4"],
                                 answer=request.POST["answer"])
        new_question.save()
        return redirect("q_home")

def q_success(request):
    return render(request, "questions/q_success.html")

def q_fail(request):
    return render(request, "questions/q_fail.html")
