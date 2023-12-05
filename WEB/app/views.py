from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse

# Create your views here.

QUESTIONS = [
    {
        'id': i,
        'title': f'Question {i}',
        'content': f'A little questiion about something {i}',
        'answers': range(i*3),
        'tags': [f'tag_{i}', f'tag_{i + 1}', f'tag_{i + 2}'],
    } for i in range(26)
]


def paginate(objects, page: str, per_page):
    temppage = 1
    if page.isdigit():
        temppage = int(page)
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
    page = request.GET.get('page', '1')
    page_obj = paginate(QUESTIONS, page, 5)
    return render(request, 'index.html', {'page_obj': page_obj})


def question(request, question_id):
    page_answ = request.GET.get('page', '1')
    page_obj = paginate(QUESTIONS[question_id]['answers'], page_answ, 5)
    return render(request, 'question.html', {'question': QUESTIONS[question_id],
                                             'page_obj': page_obj})


def signup(request):
    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')


def ask(request):
    return render(request, 'ask.html')


def settings(request):
    return render(request, 'settings.html')


def hot(request):
    page = request.GET.get('page', '1')
    page_obj = paginate(QUESTIONS, page, 5)
    return render(request, 'hot.html', {'page_obj': page_obj})


def tag(request, tag_name):
    page = request.GET.get('page', '1')
    page_obj = paginate(find_tag(QUESTIONS, tag_name), page, 5)
    return render(request, 'tag.html',
                  {
                      'page_obj': page_obj,
                      'tag': tag_name
                  })
