from django.urls import path
from . import views
from .views import register, login, catalog, ContactView, order_view, order_success_view, index_view

urlpatterns = [
    path('', index_view, name='index'),  # Главная страница
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('catalog/', catalog, name='catalog'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('order/<int:product_id>/', order_view, name='order'),  # Оформление заказа для конкретного продукта
    path('order/success/', order_success_view, name='order_success'),  # Успешное оформление заказа
]