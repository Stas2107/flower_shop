from django.urls import path
from . import views
from .views import register, login, index, catalog, ContactView

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('catalog/', catalog, name='catalog'),
    path('contact/', ContactView.as_view(), name='contact'),
]