from django.urls import path
from . import views
from .views import register, login, index, catalog, ContactView, order_view, order_success, index_view

urlpatterns = [
    path('', views.index, name='home'),
    path('', index_view, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('catalog/', catalog, name='catalog'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('order/', order_view, name='order'),
    path('order/success/', order_success, name='order_success'),
    path('order/<int:product_id>/', order_view, name='order'),
]