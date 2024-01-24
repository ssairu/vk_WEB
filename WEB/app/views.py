from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from django.http import HttpResponse

from app.models import Question, Answer

# Create your views here.

def paginate(objects_list, request, per_page=10):
    result = None
    try:
        page = request.GET.get('page', 1)
        paginator = Paginator(objects_list, per_page)
        result = paginator.page(page)
    except Exception as e:
        print(e)
    return result


def base(request):
    return render(request, 'base.html')


def index(request):
    page_obj = paginate(Question.objects.new(), request, 5)
    return render(request, 'index.html', {'page_obj': page_obj})


def question(request, question_id):
    item = get_object_or_404(Question, id=question_id)
    page_obj = paginate(item.answers, request, 5)
    return render(request, 'question.html', {'question': item,
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
    page_obj = paginate(Question.objects.hot(), request, 5)
    return render(request, 'hot.html', {'page_obj': page_obj})


def tag(request, tag_name):
    page_obj = paginate(Question.objects.by_tag(tag_name), request, 5)
    return render(request, 'tag.html',
                  {
                      'page_obj': page_obj,
                      'tag': tag_name
                  })
