from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from . models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.forms import inlineformset_factory, modelformset_factory
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    
    question = Question.objects.all()
    question_count = Question.objects.all().count()
    answers = Answer.objects.all()
    context = {'question':question,'answers':answers, 'question_count':question_count}
    
    return render(request,'Quiz/status.html',context)
#______________________________________________________________

def add_question(request):
    
    #form = QuestionForm()
    QusetionFormSet = modelformset_factory(Question,fields=('question', 'category'),extra=6)
    formset = QusetionFormSet(queryset=Question.objects.none())
    if request.method == "POST":
        #form = QuestionForm(request.POST)
        formset = QusetionFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('questions_base_page')
    
    context  = {'formset': formset}
    return render(request,'Quiz/QuestionForm.html',context)
#______________________________________________________________

def add_answers(request, pk):
    AnswerFormSet = inlineformset_factory(Question , Answer, fields=('answer','is_correct'),extra=4) 
    question = Question.objects.get(id=pk)
    formset = AnswerFormSet(instance=question)

    if request.method == 'POST':
        formset = AnswerFormSet(request.POST,instance=question)
        if formset.is_valid():
            formset.save()
            return redirect('all_questions')
    context = {'formset':formset, 'question':question}
    return render(request, 'Quiz/AnswerForm.html', context)
#______________________________________________________________

def update_question(request, pk):
    
    question = Question.objects.get(id=pk)
    form = QuestionForm(instance=question)
    
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('all_questions')
    
    context = {'form':form}
    return render(request,'Quiz/UpdateQuestion.html', context)
#______________________________________________________________


def all_questions(request):
    questions = Question.objects.all()
    context = {'questions':questions}
    return render(request, 'Quiz/questions.html', context)
#______________________________________________________________

def delete_question(request, pk):
    ques = Question.objects.get(id = pk)
    
    if request.method == "POST":
        #form = QuestionForm(request, instance=ques)
        ques.delete()
        return redirect('all_questions')
    context = {'ques':ques}
    return render(request,'Quiz/delete.html',context)
#______________________________________________________________

@login_required(login_url='login_page')
def questions_base_page(request):
    
    return render(request, "Quiz/question_base_page.html")


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('questions_base_page')
        else:
            messages.success(request,"Error Signing In")
    
    else:
        context = {}#{'form':form}
        return render(request, 'Quiz/LoginForm.html',context)

def logoutpage(request):
    logout(request)
    return redirect('login_page')
