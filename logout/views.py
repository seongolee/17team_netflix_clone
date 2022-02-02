from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def logout_view(request):
    auth.logout(request)
    return redirect('/')
    # return render(request,'logout/logout_page.html')

# @login_required             # 사용자가 로그인이 꼭 되어있어야만 접근이 가능한 함수라는 뜻
# def logout(request):
#     auth.logout(request)
#     return redirect('/')