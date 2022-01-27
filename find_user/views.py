from django.shortcuts import render

# Create your views here.
def find_user_view(request):
    return render(request,'find_pw/find_pw_page.html')

def certi_num_view(request):
    return render(request,'find_pw/certi_num_page.html')