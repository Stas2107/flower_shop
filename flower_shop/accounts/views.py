from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import RegistrationForm, CustomLoginForm
from django.contrib import messages

from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import accounts
from django.core.mail import send_mail
from django.conf import settings
from django.views import View
from django import forms


def index(request):
    return render(request, 'accounts/index.html')


def login_view(request):
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')  # Перенаправление на страницу входа
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            messages.success(request, 'Вы успешно вошли в систему!')
            return redirect('home')  # Перенаправление на главную страницу
    else:
        form = CustomLoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def catalog(request):
    flowers = accounts.objects.all()  # Получаем все цветы из базы данных
    return render(request, 'accounts/catalog.html', {'flowers': flowers})




class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ваше имя')
    email = forms.EmailField(label='Ваш Email')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')


class ContactView(View):
    form_class = ContactForm
    template_name = 'accounts/contact.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Отправка сообщения на email
            send_mail(
                f'Сообщение от {name}',
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )

            return render(request, 'accounts/contact.html', {'form': form, 'success': True})
        return render(request, self.template_name, {'form': form})