from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, UserUpdateForm
from django.contrib.auth.forms import UserChangeForm
from .models import Member

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
    u_form = UserUpdateForm()

    context = {
        'u_form': u_form
    }
    return render(request, "zenpythonpages/userprofile.html", context)

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

def delete_user(request):
    if request.method == "POST":
        to_delete = Member.objects.get(id=request.POST["id"])
        to_delete.delete()
        return redirect("home")
    return redirect("home")

def submit_q(request):
    return render(request, "zenpythonpages/submitquestion.html")

def submit_comp(request):
    return render(request, "zenpythonpages/submissioncomplete.html")