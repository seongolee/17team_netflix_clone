import base64
import hashlib
import hmac
import json
import time
import sys
import os

from django.shortcuts import render,redirect
from user.models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model      # 사용자가 데이터베이스 안에 있는지 검사하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required

#전화번호 인증관련
import requests
from random import randint
from user.models import UserModel,AuthSms


#이메일인증 관련(SMTP)
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes

# 네이버클라우드 문자보내기 설정
def send_sms(phone_number,auth_number):
    timestamp = int(time.time() * 1000)
    timestamp = str(timestamp)

    access_key = "XC1t9TAJqeTcCNYlA8Vt"  # access key id (from portal or Sub Account)
    secret_key = "i3pv3luHCavRPHhDGLiCR27w1joL7tTCRRf02w3z"  # secret key (from portal or Sub Account)
    secret_key = bytes(secret_key, 'UTF-8')

    method = "POST"
    uri = "https://sens.apigw.ntruss.com/sms/v2/services/ncp:sms:kr:279677688555:17_netflix_clone/messages"

    message = method + " " + uri + "\n" + timestamp + "\n" + access_key
    message = bytes(message, 'UTF-8')
    signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())

    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "x-ncp-apigw-timestamp": timestamp ,
        "x-ncp-iam-access-key": "XC1t9TAJqeTcCNYlA8Vt",
        "x-ncp-apigw-signature-v2": signingKey
    }

    body = {
        "type":"SMS",
        "contentType":"COMM",
        "from":"01097590231",
        "content":"[테스트] 인증번호 [{}]를 입력해주세요.".format(auth_number),
        "messages":[{"to":phone_number}]
    }

    requests.post("https://sens.apigw.ntruss.com/sms/v2",data = body, headers= headers)

# Create your views here.
def find_user_view(request):
    if request.method == 'POST':
        user_info = request.POST.get('send-info', '')
        type_info = user_info.find('@')
        print(user_info)
        print(type_info)

        if type_info == -1:
            auth_num = randint(1000, 10000)
            exist_phone = UserModel.objects.filter(phone_number=user_info)
            model_phone = UserModel.objects.get(phone_number=user_info)

            if exist_phone:
                exist_auth = AuthSms.objects.filter(phone_num=user_info)
                if exist_auth:
                    get_auth = AuthSms.objects.get(phone_num=user_info)
                    get_auth.auth_number = auth_num
                    get_auth.save()
                    send_sms(phone_number=user_info, auth_number=auth_num)
                    print('발송 성공')

                else:
                    AuthSms.objects.create(phone_num=model_phone, auth_number=auth_num)
                    send_sms(phone_number=user_info, auth_number=auth_num)
                    print('발송 성공')

                return render(request, 'find_pw/certi_num_page.html')
            else:
                return redirect('/find-pw')


        else:
            user = UserModel.objects.filter(email = user_info)
            auth_num = randint(1000, 10000)
            if user:
                current_site = get_current_site(request)
                message = f'인증번호 {auth_num}'
                mail_title = "이메일 확인 인증번호 발송"
                mail_to = request.POST["send-info"]
                email = EmailMessage(mail_title, message, to=[mail_to])
                email.send()

                return render(request,'find_pw/certi_num_page.html')
    elif request.method == 'GET':
        return render(request, 'find_pw/find_pw_page.html')


def certi_num_view(request):
    return render(request,'find_pw/certi_num_page.html')

def set_pw_view(request):
    return render(request,'find_pw/set_pw_page.html')