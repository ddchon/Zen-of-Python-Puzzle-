from django.shortcuts import render, redirect
from .models import Question
from zenpythonpages.models import Member


def q_home(request):
    if request.user.is_authenticated:
        member = Member.objects.get(id=request.user.id)
        correct_answers = []
        print(correct_answers)
        if len(member.answered_comp) > 0:
            for a in member.answered_comp.split(","):
                print(a)
            if int(a) < 10:
                correct_answers.append("0" + str(a))
            else:
                correct_answers.append(str(a)) 

        context = {
            "correct_answers": correct_answers,
        }
        print(correct_answers)
    # print(member.answered_comp)
        return render(request, "questions/questionshome.html")
    else:
        return redirect('/accounts/login')

    return render(request, "questions/questionshome.html", context=context)
       
def ind_questions(request, id):
    question = Question.objects.get(id=id)
    context = {
        "question": question
    }
    print(question)
    
    return render(request, "questions/ind_question.html", context=context)

def submitted_answer(request, id):
    if request.method == "POST":
        q = Question.objects.get(id=request.POST['question'])
        if q.answer == request.POST["answerGroup"]:
            member = Member.objects.get(id=request.user.id)
            if not str(request.POST['question']) in str(member.answered_comp).split(","):
                if len(str(member.answered_comp)) == 0:
                    member.answered_comp += str(request.POST['question'])
                else:
                    member.answered_comp += "," + str(request.POST['question'])
   
                member.save()
                return redirect("q_success")

            else:
                return redirect("q_success")
        else:
            return redirect("q_fail")

def new_question(request):
    if request.method == "POST":
        question_list = Question(question=request.POST["question"],
                                 p_answer1=request.POST["p_answer1"],
                                 p_answer2=request.POST["p_answer2"],
                                 p_answer3=request.POST["p_answer3"],
                                 p_answer4=request.POST["p_answer4"],
                                 answer=request.POST["answer"])
        question_list.save()
        return redirect("q_home")

def q_success(request):
    return render(request, "questions/q_success.html")

def q_fail(request):
    return render(request, "questions/q_fail.html")
