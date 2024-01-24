from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.urls import reverse

from app.forms import LoginForm, AddAnswerForm
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
    return result, page


def base(request):
    return render(request, 'base.html')


def index(request):
    page_obj = paginate(Question.objects.new(), request, 5)
    return render(request, 'index.html', {'page_obj': page_obj})


def question(request, question_id):
    item = get_object_or_404(Question, id=question_id)
    page_obj, page = paginate(item.answers, request, 5)

    if request.method == 'GET':
        form = AddAnswerForm()
    if request.method == "POST":
        form = AddAnswerForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                current_user = request.user
                user = User.objects.get(username=current_user.username).profile

                data = form.cleaned_data
                Answer.objects.create(author=user, question=item, text=data["answer"], accepted=False)

                last_answer_id = Answer.objects.latest('id').id
                redirect_url = f'/question/{question_id}?page={page_obj.paginator.num_pages}#{last_answer_id}'
                return redirect(redirect_url)
            else:
                form.add_error('answer', "You must be logged in!")

    return render(request, 'question.html', {'question': item,
                                             'page_obj': page_obj,
                                             'form': form})


def signup(request):
    return render(request, 'signup.html')


def log_in(request):
    if request.method == 'GET':
        form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user is not None:
                login(request, user)
                return redirect(request.GET.get('continue', '/'))
            else:
                form.add_error(None, "Wrong password or user doesn't exist")

    return render(
        request,
        'login.html', context={"form": form}
    )

def log_out(request):
    auth.logout(request)
    return redirect(reverse('login'))


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
