from django.shortcuts import render
from user.models import UserModel, ProfileId
from main.models import Genre, Video, VideoModal


# Create your views here.
def sign_up(request):
    return render(request, 'sign_up/sign_up.html')
