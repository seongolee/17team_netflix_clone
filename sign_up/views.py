from django.http import HttpResponse
from django.shortcuts import render, redirect
from user.models import UserModel
from django.contrib.auth.decorators import login_required
import json


# Create your views here.
def sign_up_check(request):
    if request.method == 'GET':
        return render(request, 'sign_up/sign_up_check.html', {'test': 'hi'})
    elif request.method == 'POST':
        email = request.POST.get('email')
        is_email = UserModel.objects.filter(username=email)

        if is_email:
            site = '/login'
        else:
            site = '/kr/signup'

        request.session['email'] = email

        return redirect(site)


@login_required
def sign_up_registration(request):
    # email = request.session['email']
    #
    # del request.session['email']

    return render(request, 'sign_up/sign_up_registration.html')

