from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    return render(request,'login/login_page.html')

# @login_required             # 사용자가 로그인이 꼭 되어있어야만 접근이 가능한 함수라는 뜻
def login(request):

    return render(request, 'mainpage_html/main.html')