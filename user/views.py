from django.shortcuts import render
from .models import UserModel,ProfileId
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def create_profile():

    user = UserModel.objects.create_user(username=username, password=password, email =email,)
    for i in range(5):
        ProfileId.objects.create(profile_id=user.userid +i)