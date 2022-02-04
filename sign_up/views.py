from django.http import HttpResponse
from django.shortcuts import render, redirect
from user.models import UserModel, ProfileId
from django.contrib.auth.decorators import login_required
import json


# Create your views here.
def sign_up_check(request):
    if request.method == 'GET':
        return render(request, 'sign_up/sign_up_check.html')
    elif request.method == 'POST':
        email_phone = request.POST.get('email_phone')

        email_phone_check = email_phone.find('@')
        email = ''
        phone_number = ''

        if email_phone_check == -1:
            email_phone_check = UserModel.objects.filter(phone_number=email_phone)
            phone_number = email_phone
        else:
            email_phone_check = UserModel.objects.filter(email=email_phone)
            email = email_phone

        if email_phone_check:
            return redirect('/login')
        else:
            return render(request, 'sign_up/sign_up_registration.html', {'email': email, 'phone_number': phone_number})


def sign_up_registration(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        phone_number = str(request.POST.get('phone-number'))
        phone_number = phone_number.replace('-', '')

        user_id = UserModel.objects.create_user(email=email, phone_number=phone_number, username=username,
                                                password=password)
        ProfileId.objects.create(user_id=user_id)

        return redirect('/login')
