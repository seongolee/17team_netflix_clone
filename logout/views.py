from django.shortcuts import render

# Create your views here.
def logout_view(request):
    return render(request,'logout/logout_page.html')