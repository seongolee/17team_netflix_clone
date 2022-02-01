import base64, hashlib, hmac, time,json
from django.contrib import auth

#비밀번호 변경 함수
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse

from django.shortcuts import render, redirect
from user.models import UserModel, AuthSms


#전화번호 인증관련
import requests
from random import randint
from user.models import UserModel


#이메일인증 관련(SMTP)
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage


def make_signatures(timestamp):
    secret_key = "ewrEcW9qG7mQTfoV2yJCTkXjwMVeqN8FS7WW5bc2"  # secret key (from portal or Sub Account)
    secret_key = bytes(secret_key, 'UTF-8')
    uri = '/sms/v2/services/ncp:sms:kr:279717467536:test/messages'
    message = "POST" + " " + uri + "\n" + timestamp + "\n" + 'g5Zmd1j2xKyAdx391t4p'
    message = bytes(message, 'UTF-8')
    signing_key = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())

    return signing_key


# 네이버클라우드 문자보내기 설정
def send_sms(phone_number, auth_number):
    timestamp = str(int(time.time() * 1000))
    signing_key = make_signatures(timestamp)

    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "x-ncp-apigw-timestamp": timestamp ,
        "x-ncp-iam-access-key": "g5Zmd1j2xKyAdx391t4p",
        "x-ncp-apigw-signature-v2": signing_key
    }

    context = {
        "type": "SMS",
        "contentType": "COMM",
        "countryCode": "82",
        "from": "01096551409",
        "content": "[테스트] 인증 번호 [{}]를 입력해주세요.".format(auth_number),
        "messages": [{"to": phone_number}]
    }

    encoded_data = json.dumps(context)
    url = 'https://sens.apigw.ntruss.com/sms/v2/services/ncp:sms:kr:279717467536:test/messages'

    response = requests.post(url, headers=headers, data=encoded_data)

    if not response.ok:
        print(response)
    else:
        print('확인')

    return True


# Create your views here.
def find_user_view(request):
    if request.method == 'POST':
        user_radio = request.POST.get('type_choice')
        print(f'user_radio: {user_radio}')

        if user_radio == 'MSG':
            user_msg = request.POST.get('send-msg')
            auth_num = randint(1000, 10000)
            exist_phone = UserModel.objects.filter(phone_number=user_msg)


            if exist_phone:
                exist_auth = AuthSms.objects.filter(phone_number=user_msg)
                print(exist_phone)
                if exist_auth:
                    get_auth = AuthSms.objects.get(phone_number=user_msg)
                    get_auth.auth_number = auth_num
                    get_auth.save()
                    send_sms(phone_number=user_msg, auth_number=auth_num)
                    print('발송 성공1')

                else:
                    AuthSms.objects.create(phone_number=user_msg, auth_number=auth_num)
                    print(user_msg, auth_num)
                    send_sms(phone_number=user_msg, auth_number=auth_num)
                    print('발송 성공2')

                return render(request, 'find_pw/certi_num_page.html')
            else:
                return redirect('/find-user')


        else:
            user_email = request.POST.get('send-email')
            user = UserModel.objects.filter(email=user_email)
            auth_num = randint(1000, 10000)
            if user:
                exist_sms = UserModel.objects.get(email=user_email)
                find_info = AuthSms.objects.filter(phone_number=exist_sms.phone_number)
                if find_info:
                    get_auth = AuthSms.objects.get(phone_number=exist_sms.phone_number)
                    get_auth.auth_number = auth_num
                    get_auth.save()
                    current_site = get_current_site(request)
                    message = f'인증번호 {auth_num}'
                    mail_title = "이메일 확인 인증번호 발송"
                    mail_to = request.POST["send-email"]
                    email = EmailMessage(mail_title, message, to=[mail_to])
                    email.send()

                else:
                    AuthSms.objects.create(phone_number=exist_sms.phone_number, auth_number=auth_num)
                    current_site = get_current_site(request)
                    message = f'인증번호 {auth_num}'
                    mail_title = "이메일 확인 인증번호 발송"
                    mail_to = request.POST["send-email"]
                    email = EmailMessage(mail_title, message, to=[mail_to])
                    email.send()

                request.session['user_email'] = user_email
                return redirect('/find-user/certi')
            else:
                print('문자 전송 실패')
                return render(request, 'find_pw/find_pw_page.html')

    elif request.method == 'GET':

        return render(request, 'find_pw/find_pw_page.html')


def auth_user(request):
    user_radio = request.GET.get('input_type')
    user_send = request.GET.get('input_val')

    if user_radio == 'EMAIL':
        exist_user = UserModel.objects.filter(email=user_send)
    else:
        exist_user = UserModel.objects.filter(phone_number=user_send)

    result = False
    if exist_user:
        result = True


    context = {'result': result}
    return HttpResponse(json.dumps(context), content_type="application/json")

def auth_num(request):
    auth_num = request.GET.get('auth_number')
    user_info = request.session['user_info']
    type_info = user_info.find('@')
    exist_auth = ''
    if type_info == -1 :
        exist_auth = AuthSms.objects.filter(phone_number=user_info)
    else :
        exist_user = UserModel.objects.get(email=user_info)
        exist_auth = AuthSms.objects.filter(phone_number=exist_user.phone_number)

    result = False

    exist_auth_num = list(exist_auth.values('auth_number'))[0]
    print(exist_auth_num)

    if exist_auth_num['auth_number'] == auth_num:
        result = True

    context = {'result': result}
    return HttpResponse(json.dumps(context), content_type="application/json")


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