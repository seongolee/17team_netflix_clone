from django.shortcuts import render, redirect
from login.views import login_required
from django.contrib import auth



# Create your views here.
def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/main')
    else:
        return redirect('/kr')


# main_view

def main_view(request):
    return render(request, 'mainpage_html/main.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')
