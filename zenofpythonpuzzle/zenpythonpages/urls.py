
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("new_user/", views.new_user, name="new_user"),
    path("profile/", views.profile, name="profile"),
    path("profile/edit", views.edit_profile, name="editprofile"),
    path("submit_q/", views.submit_q, name="submit_q"),
    path("delete_user/<username>", views.delete_user, name="delete_user"),
]
