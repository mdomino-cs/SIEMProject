from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def logs(request):
    return render(request, 'logs.html')

def alerts(request):
    return render(request, 'alerts.html')

def settings(request):
    return render(request, 'settings.html')

urlpatterns = [
    # Serve the site root at '/'
    path('', home, name='home'),
    path('logs/', logs, name='logs'),
    path('alerts/', alerts, name='alerts'),
    path('settings/', settings, name='settings'),
]
