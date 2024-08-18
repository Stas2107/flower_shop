from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, OrderForm
from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'shop/register.html', {'form': form})

@login_required  # Добавляем декоратор для ограничения доступа
def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('home')
    else:
        form = OrderForm()
    return render(request, 'shop/order.html', {'form': form})