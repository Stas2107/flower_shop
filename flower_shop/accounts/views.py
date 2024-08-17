from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from .forms import RegisterForm


def index(request):
    return HttpResponse('Привет, это главная страница')


def login_view(request):
    return HttpResponse('Привет, это страница логина')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Перенаправление на главную страницу после регистрации
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})