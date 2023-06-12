from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.email_create, name='email_create'),
    path('list/', views.email_list, name='email_list'),
]