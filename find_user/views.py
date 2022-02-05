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

from main.models import Video,VideoModal,Genre
import csv

def make_signatures(timestamp):
    secret_key = secrets['SMS']['SECRET_KEY'] # secret key (from portal or Sub Account)
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

    requests.post(url, headers=headers, data=encoded_data)


# find-user
def find_user_view(request):
    if request.method == 'GET':
        return render(request, 'find_pw/find_pw_page.html')

    elif request.method == 'POST':
        user_radio = request.POST.get('type_choice')

        auth_num = randint(1000, 10000)
        request.session['auth_number'] = auth_num
        # ridao 버튼이 MSG인 경우
        if user_radio == 'MSG':
            user_msg = request.POST.get('send-msg')

            # 세션에 번호를 담는 것
            request.session['user_info'] = user_msg

            AuthSms.objects.update_or_create(phone_number=user_msg, defaults={"auth_number": auth_num})
            send_sms(user_msg, auth_num)

            return redirect('/find-user/certi')
        else:
            user_email = request.POST.get('send-email')

            request.session['user_info'] = user_email

            exist_sms = UserModel.objects.get(email=user_email)
            AuthSms.objects.update_or_create(phone_number=exist_sms.phone_number, defaults={"auth_number": auth_num})

            return redirect('/find-user/certi')


# send-email
def send_email(request):
    user_info = request.session['user_info']
    phone_email_check = user_info.find('@')
    auth_number = request.session['auth_number']

    if not (phone_email_check == -1):
        message = f'인증번호 {auth_number}'
        mail_title = "이메일 확인 인증번호 발송"
        mail_to = user_info
        email = EmailMessage(mail_title, message, to=[mail_to])
        email.send()
    print('인증번호 확인 페이지', auth_number)

    return HttpResponse()


# auth-user
# DB에 저장되어있는 유저인지 확인
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


# 인증 번호 체크
def auth_num(request):

    user_auth_num = request.GET.get('auth_number')
    user_info = request.session['user_info']
    phone_email_check = user_info.find('@')

    if not (phone_email_check == -1):
        user_info = UserModel.objects.get(email=user_info).phone_number

    auth_num = str(AuthSms.objects.get(phone_number=user_info).auth_number)

    result = False

    if auth_num == user_auth_num:
        result = True

    context = {'temp': result}
    return HttpResponse(json.dumps(context), content_type="application/json")


# certi-num
def certi_num_view(request):


    if request.method == 'GET':
        return render(request, 'find_pw/certi_num_page.html')


# 비밀번호 변경
def set_pw_view(request):
    if request.method == 'GET':
        user_info = request.session['user_info']
        type_info = user_info.find('@')
        if type_info == -1:
            get_email = UserModel.objects.get(phone_number=user_info)
            return render(request, 'find_pw/set_pw_page.html',{'email':get_email.email})
        else:
            return render(request, 'find_pw/set_pw_page.html', {'email': user_info})

    elif request.method == 'POST':
        user_info = request.session['user_info']
        new_password = request.POST.get('newPassword', '')
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

def add_data(request):
    path = "C:/Users/Administrator/Downloads/video_table_data.csv"
    file = open(path)
    reader = csv.reader(file)
    for row in reader:
        videos = Video.objects.create(video_title=row[0],video_clip =row[1],age_limit_logo =row[2])

        genre = row[6]
        genres = genre.split('/')
        del genres[-1]
        for i in range(len(genres)):
            total_genre = Genre.objects.get(genre=genres[i])
            videos.genre_id.add(*total_genre)

        VideoModal.objects.create(video_id=videos.id, video_description= row[3])
    return HttpResponse('create data')