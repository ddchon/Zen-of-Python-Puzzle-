
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Member

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=60, help_text="Required. Add a valid email address")
    bio = forms.CharField(max_length=100)

    class Meta:
        model = Member
        fields = ("email", "username", "password1", "password2", "first_name", "last_name", "bio")

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=60, help_text="Required. Add a valid email address")
    bio = forms.CharField(max_length=100)

    class Meta:
        model = Member
        fields = ("email", "username", "first_name", "last_name", "bio")

# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Member
#         field = ['image']