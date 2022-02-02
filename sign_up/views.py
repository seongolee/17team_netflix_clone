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

        if email_phone_check == -1:
            email_phone_check = UserModel.objects.filter(phone_number=email_phone)
        else:
            email_phone_check = UserModel.objects.filter(email=email_phone)

        if email_phone_check:
            site = '/login'
        else:
            site = '/kr/signup'

        request.session['email_phone'] = email_phone

        return redirect(site)


def sign_up_registration(request):
    email_phone = request.session['email_phone']
    if request.method == 'GET':
        return render(request, 'sign_up/sign_up_registration.html', {'email_phone': email_phone})
    elif request.method == 'POST':
        email_phone = request.POST.get('email-phone')
        password = request.POST.get('password')
        username = request.POST.get('username')
        user_id = ''

        email_phone_check = email_phone.find('@')
        if email_phone_check == -1:
            user_id = UserModel.objects.create_user(phone_number=email_phone, username=username, password=password)
        else:
            user_id = UserModel.objects.create_user(email=email_phone, username=username, password=password)

        ProfileId.objects.create(user_id=user_id)

        return redirect('/login')



