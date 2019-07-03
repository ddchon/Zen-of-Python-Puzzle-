from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, UserUpdateForm
from django.contrib.auth.forms import UserChangeForm
from .models import Member, SubmitQuestion

def index(request):
    context = {}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('profile')
        else:
            context['registration_form'] = form
    return render(request, "zenpythonpages/home.html")

def new_user(request):
    context = {}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('profile')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, "zenpythonpages/signup.html", context)

def profile(request):
   member = Member.objects.get(username=request.user.username)
   answer_perc = int(len(member.answered_comp.split(",")) / 19) * 100
   context = {
           "answer_perc" : answer_perc
   }
   print(answer_perc)
   return render(request, "zenpythonpages/userprofile.html", context=context)

def edit_profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
        context = { 
            "form": form
        }
    return render(request, "zenpythonpages/editprofile.html", context)

def delete_user(request, username):
    try:
        to_delete = Member.objects.get(username=username)
        to_delete.delete()
        print("User Deleted")
    except Member.DoesNotExit:
        print("User Does Not Exist")
        return redirect("profile")
    return redirect("home")

def submit_q(request):
    if request.method == "POST":
        member = Member.objects.get(username=request.user.username)
        new_q = SubmitQuestion(title=request.POST["title"], question=request.POST["question"], member=member)
        print(new_q)
        new_q.save()
        return redirect("submit_comp")
    return render(request, "zenpythonpages/submitquestion.html")

def submit_comp(request):
    return render(request, "zenpythonpages/submissioncomplete.html")

