from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

urlpatterns = [
    # Serve the site root at '/'
    path('', index, name='index'),
    # Optional convenience route; include trailing slash for common behavior
    path('index/', index, name='index_alt'),
]
