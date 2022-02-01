import base64, hashlib, hmac, time
from django.contrib import auth

#비밀번호 변경 함수
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from django.shortcuts import render, redirect
from user.models import UserModel, AuthSms


#전화번호 인증관련
import requests
from random import randint
from user.models import UserModel


#이메일인증 관련(SMTP)
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage


# 네이버클라우드 문자보내기 설정
def send_sms(phone_number, auth_number):
    timestamp = int(time.time() * 1000)
    timestamp = str(timestamp)

    access_key = "XC1t9TAJqeTcCNYlA8Vt"  # access key id (from portal or Sub Account)
    secret_key = "i3pv3luHCavRPHhDGLiCR27w1joL7tTCRRf02w3z"  # secret key (from portal or Sub Account)
    secret_key = bytes(secret_key, 'UTF-8')

    method = "POST"
    uri = "https://sens.apigw.ntruss.com/sms/v2/services/ncp:sms:kr:279677688555:17_netflix_clone/messages"

    message = method + " " + uri + "\n" + timestamp + "\n" + access_key
    message = bytes(message, 'UTF-8')
    signing_key = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())

    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "x-ncp-apigw-timestamp": timestamp ,
        "x-ncp-iam-access-key": "XC1t9TAJqeTcCNYlA8Vt",
        "x-ncp-apigw-signature-v2": signing_key
    }

    body = {
        "type":"SMS",
        "contentType":"COMM",
        "from":"01097590231",
        "content":"[테스트] 인증번호 [{}]를 입력해주세요.".format(auth_number),
        "messages":[{"to": phone_number}]
    }

    requests.post("https://sens.apigw.ntruss.com/sms/v2",data = body, headers= headers)

# Create your views here.
def find_user_view(request):
    if request.method == 'POST':
        user_info =request.POST.getlist('send-info', '')
        print(f'user_info: {user_info}')

        user_email = user_info[0]
        user_num = user_info[1]

        if user_email == '':
            auth_num = randint(1000, 10000)
            exist_phone = UserModel.objects.filter(phone_number=user_num)

            if exist_phone:
                model_phone = UserModel.objects.get(phone_number=user_num)

                exist_auth = AuthSms.objects.filter(phone_number=user_num)
                if exist_auth:
                    get_auth = AuthSms.objects.get(phone_number=user_num)
                    get_auth.auth_number = auth_num
                    get_auth.save()
                    send_sms(phone_number=user_info, auth_number=auth_num)
                    print('발송 성공')

                else:
                    AuthSms.objects.create(phone_number=model_phone, auth_number=auth_num)
                    send_sms(phone_number=user_info, auth_number=auth_num)
                    print('발송 성공')

                return render(request, 'find_pw/certi_num_page.html')
            else:
                return redirect('/find-user')


        else:
            user = UserModel.objects.filter(email = user_email)
            auth_num = randint(1000, 10000)
            if user:
                exist_sms = UserModel.objects.get(email = user_email)
                find_info = AuthSms.objects.filter(phone_number=exist_sms.phone_number)
                if find_info :
                    get_auth = AuthSms.objects.get(phone_number=exist_sms.phone_number)
                    get_auth.auth_number = auth_num
                    get_auth.save()
                    current_site = get_current_site(request)
                    message = f'인증번호 {auth_num}'
                    mail_title = "이메일 확인 인증번호 발송"
                    mail_to = request.POST["send-info"]
                    email = EmailMessage(mail_title, message, to=[mail_to])
                    email.send()

                else:
                    AuthSms.objects.create(phone_number=exist_sms.phone_number, auth_number=auth_num)
                    current_site = get_current_site(request)
                    message = f'인증번호 {auth_num}'
                    mail_title = "이메일 확인 인증번호 발송"
                    mail_to = request.POST["send-info"]
                    email = EmailMessage(mail_title, message, to=[mail_to])
                    email.send()

                request.session['user_info']= user_email
                return redirect('/find-user/certi')
            else:
                print('문자 전송 실패')
                return render(request, 'find_pw/find_pw_page.html')

    elif request.method == 'GET':

        return render(request, 'find_pw/find_pw_page.html')


def certi_num_view(request):
    user_info = request.session['user_info']
    if request.method == 'POST':
        type_info = user_info.find('@')
        print(type_info)
        if type_info == -1:
            auth_num = request.POST.get('certi_num', '')
            get_auth = AuthSms.objects.get(phone_number=user_info)

            if get_auth.auth_number == int(auth_num):
                print('일치')
                return redirect('/find-user/set-pw')
            else:
                print('불일치')
                return redirect('/find-user/certi')

        else:
            auth_num = request.POST.get('certi_num', '')
            get_phone = UserModel.objects.get(email=user_info)
            get_auth = AuthSms.objects.get(phone_number=get_phone.phone_number)
            print(auth_num)
            print(get_phone.phone_number)
            if get_auth.auth_number == int(auth_num):
                print('일치')
                return redirect('/find-user/set-pw')
            else:
                print('불일치')
                return redirect('/find-user/certi')

    elif request.method == 'GET':
        return render(request, 'find_pw/certi_num_page.html')

def set_pw_view(request):

    if request.method == 'POST':
        user_info = request.session['user_info']
        new_password = request.POST.get('newPassword','')
        type_info = user_info.find('@')
        if type_info == -1:
            user = UserModel.objects.get(phone_number=user_info)
            user.set_password(new_password)
            user.save()
            response = redirect('/login')
            response.set_cookie('password',new_password)
            return response
        else :
            user = UserModel.objects.get(email=user_info)
            user.set_password(new_password)
            user.save()
            response = redirect('/login')
            return response

    elif request.method == 'GET':
        user_info = request.session['user_info']
        type_info = user_info.find('@')
        if type_info == -1:
            get_email = UserModel.objects.get(phone_number=user_info)
            return render(request, 'find_pw/set_pw_page.html',{'email':get_email.email})
        else:
            return render(request, 'find_pw/set_pw_page.html', {'email': user_info})