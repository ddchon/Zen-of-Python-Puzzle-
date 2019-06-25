
from django.urls import path

from . import views

urlpatterns = [
    path("q_home/", views.q_home, name="q_home"),
    path("ind_questions/", views.ind_questions, name="ind_questions"),
    path("q_success", views.q_success, name="q_success"),
    path("q_fail", views.q_fail, name="q_fail")
]
