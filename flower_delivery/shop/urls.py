from django.urls import path
from .views import home, register, order

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('order/', order, name='order'),
]