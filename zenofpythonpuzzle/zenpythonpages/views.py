from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, UserUpdateForm
from django.contrib.auth.forms import UserChangeForm
from .models import Member, SubmitQuestion
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    return render(request, "zenpythonpages/home.html")

def new_user(request):
    context = {}

    if request.POST:
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            messages.success(request, "Your account has been created!")
            return redirect('profile')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, "zenpythonpages/signup.html", context)

# @login_required(login_url='/')    
def profile(request):
    if request.user.is_authenticated:
    	member = Member.objects.get(username=request.user.username)
    	answer_perc = 0
    	if len(member.answered_comp) != 0:
     	   answer_perc = (len(member.answered_comp.split(",")) * 100) / 19
    
    	context = {
    	        "answer_perc" : answer_perc
    	}
    	return render(request, "zenpythonpages/userprofile.html", context=context)

    else:
        return redirect('/accounts/login')

def edit_profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
        context = { 
            "form": form
        }
    return render(request, "zenpythonpages/editprofile.html", context=context)

def delete_user(request, username):
    try:
        to_delete = Member.objects.get(username=username)
        to_delete.delete()
        messages.warning(request, f"Your account has been deleted!")
    except Member.DoesNotExist:
        print("User Does Not Exist")
        return redirect("profile")
    return redirect("home")

def submit_q(request):
    member = Member.objects.get(username=request.user.username)
    all_questions = SubmitQuestion.objects.exclude(member=member)
    all_questions = all_questions[::-1]

    my_questions = SubmitQuestion.objects.filter(member=member)
    my_questions = my_questions[::-1]

    context = {
        "all_questions": all_questions[0:9],
        "my_questions": my_questions[0:9]
    }

    if request.method == "POST":
        new_q = SubmitQuestion(title=request.POST["title"], question=request.POST["question"], member=member)
        new_q.save()
        messages.success(request, f"Your question has been successfully submitted!")
        return redirect("submit_q")
    return render(request, "zenpythonpages/submitquestion.html", context=context)

