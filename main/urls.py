from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path("", FirstView.as_view(), name="home"),
    path("register/", Register.as_view(), name="register"),
    path("ways/", ways, name="ways"),
    path("quiz/<slug>", quiz, name="main"),
    path("check", check, name="check"),
    path("logic_quiz/<int:logig_quiz_id>", LogicQuizView.as_view(), name="logic_quiz"),
    path("results", results, name="results"),
    path("view/results", view_results, name="view_results"),
    path("<str:ways_slug>/users/list", users_list, name="users_list"),
    path("user/<int:user_id>/results", user_results, name="user_results"),
]
