from django.shortcuts import render
from django.contrib import auth

# Create your views here.
def login_view(request):
    return render(request,'login/login_page.html')


def login(request):
    auth.login(request)
    return render(request, 'mainpage_html/main.html')