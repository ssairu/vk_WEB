from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse

# Create your views here.

QUESTIONS = [
    {
        'id': i,
        'title': f'Question {i}',
        'content': f'A little questiion about something {i}',
        'answers': range(5),
        'tags': [f'tag_{i}', f'tag_{i + 1}', f'tag_{i + 2}'],
    } for i in range(10)
]


def paginate(objects, page, per_page):
    temppage = 1
    if int == type(page):
        temppage = page
    paginator = Paginator(objects, per_page)
    return paginator.page(temppage)

def find_tag(questions, tag):
    res = []
    for q in questions:
        for t in q['tags']:
            if t == tag:
                res.append(q)
    return res


def base(request):
    return render(request, 'base.html')


def index(request):
    # page = request.GET.get('page', 1)
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


def hot(request):
    return render(request, 'hot.html', {'questions': paginate(QUESTIONS, 1, 5)})


def tag(request, tag_name):
    return render(request, 'tag.html',
                  {
                      'questions': paginate(find_tag(QUESTIONS, tag_name), 1, 5),
                   'tag': tag_name})
