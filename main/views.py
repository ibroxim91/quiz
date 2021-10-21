# from typing import ContextManager
from django.shortcuts import render, redirect
from django.views import View
# from django.core.paginator import Paginator
from main.models import Quiz, User, Ways,Results,Answer,LogicQuiz
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

class FirstView(View):
    def get(self, request):
        return render(request, 'home.html')

class Register(View):
    def get(self, request):
        return render(request, 'register.html')
    
    def post(self, request):
        password = request.POST.get('password')
        try:
            user = User.objects.get(unique_field=password)
            if Results.objects.filter(user=user).exists():
                messages.add_message(request,messages.WARNING,"Bu paroldan foydalanish muddati tugagan")    
                return redirect("main:register")
            request.session['user_id'] = user.id
            return redirect('/ways')
        except:
            messages.add_message(request,messages.WARNING,"Bunday parol mavjud emas")    
            return redirect("main:register")

def ways(request):
    cats = Ways.objects.all()
    context = {
        'cats':cats
    }
    return render(request, 'ways.html', context)

def quiz(request, slug):
    ways = Ways.objects.get(slug=slug)
    quizz = Quiz.objects.filter(ways=ways)
    context = {
    'quiz':quizz,
    }
    for i in quizz:
        if i == True:
            i+=User.true_a
    return render(request, 'tests.html', context)

def check(request):
    data = request.POST.copy()
    data.pop('csrfmiddlewaretoken')
    user = User.objects.get(id=int(request.session['user_id']))
    for key,value in data.items():
        quiz = Quiz.objects.get(id=int(key))
        answer = Answer.objects.get(id=int(value))
        Results.objects.create(user=user,quiz=quiz,user_answer=answer)
    return HttpResponseRedirect(reverse("main:logic_quiz", kwargs={"logig_quiz_id":0})) 

class LogicQuizView(View):
    def get(self,request,logig_quiz_id):
        user = User.objects.get(id=int(request.session['user_id']))
        user_results = Results.objects.filter(user=user)
        x = user_results.filter(user_answer__true_answer=True).count()
        if logig_quiz_id:
            quiz = LogicQuiz.objects.get(id=int(logig_quiz_id))
            try:
                l_quiz = quiz.get_next_by_date()
            except:
                return redirect("main:results")    

        else:
            l_quiz = LogicQuiz.objects.earliest('date')
        return render(request,"logic_quiz.html",{"l_quiz":l_quiz})

    def post(self,request,logig_quiz_id):
        user = User.objects.get(id=int(request.session['user_id']))
        quiz = LogicQuiz.objects.get(id=request.POST['quiz_id'])
        Results.objects.create(user=user,logic_quiz=quiz,logic_answer=request.POST['answer'])
        return HttpResponseRedirect(reverse("main:logic_quiz", kwargs={"logig_quiz_id":quiz.id}))

def results(request):
    user = User.objects.get(id=int(request.session['user_id']))
    user_results = Results.objects.filter(user=user)
    x = user_results.filter(user_answer__true_answer=True).count()
    return render(request,"results.html",{"results":user_results,"true_answers":x})

def view_results(request):
    cats = Ways.objects.all()
    context = {
        'cats':cats,
        "view_result":True
    }
    return render(request, 'ways.html', context)


def users_list(request,ways_slug):
    ways = Ways.objects.get(slug=ways_slug)
    users = User.objects.filter(ways=ways)
    context = {"users":users,"ways":ways}
    return render(request, 'users_list.html', context)

def user_results(request,user_id):
    user = User.objects.get(id=user_id)
    print(user.name)
    user_results = Results.objects.filter(user=user)
    x = user_results.filter(user_answer__true_answer=True).count()
    context = {"results":user_results,"true_answers":x,"user":user}
    return render(request,"results.html",context)  
