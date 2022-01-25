from django.shortcuts import render, redirect

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