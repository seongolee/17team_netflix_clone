from django.shortcuts import render

# Create your views here.
def find_user_view(request):
    return render(request,'find_pw/find_pw_page.html')