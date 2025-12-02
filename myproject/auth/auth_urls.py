from auth_forms import UserLoginForm
from django.urls import path
from django.contrib.auth import views as auth_views
from django.shortcuts import render

def login_view(request):
    form = UserLoginForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        auth_views.LoginView.as_view()(request)
    return render(request, 'auth/login.html', {'form': form})