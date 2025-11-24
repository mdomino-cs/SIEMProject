from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

urlpatterns = [
    path('index', index, name='index'),
]
