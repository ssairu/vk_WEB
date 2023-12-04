from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse

# Create your views here.

QUESTIONS = [
    {
        'id': i,
        'title': f'Question {i}',
        'content': f'A little questiion about something {i}',
        'answers': range(5)
    } for i in range(10)
]


def base(request):
    return render(request, 'base.html')


def paginate(objects, page, per_page):
    temppage = 1
    if int == type(page):
        temppage = page
    paginator = Paginator(objects, per_page)
    return paginator.page(temppage)


def index(request):
    #page = request.GET.get('page', 1)
    return render(request, 'index.html', {'questions': paginate(QUESTIONS, 1, 5)})


def question(request, question_id):
    return render(request, 'question.html', {'question': QUESTIONS[question_id]})


def signup(request):

    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')


def ask(request):
    return render(request, 'ask.html')


def settings(request):
    return render(request, 'settings.html')
