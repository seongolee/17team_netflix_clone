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
from user.tokens import account_activation_token
from django.utils.encoding import force_bytes

# 네이버클라우드 문자보내기 설정
def send_sms(phone_number,auth_number):
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'x-ncp-auth-key': f'XC1t9TAJqeTcCNYlA8Vt',
        'x-ncp-service-secret': f'i3pv3luHCavRPHhDGLiCR27w1joL7tTCRRf02w3z ',
    }

    SMS_URL = 'https://api-sens.ncloud.com/v1/sms/services/ncp:sms:kr:279677688555:17_netflix_clone/messages/'

    data = {
        'type': 'SMS',
        'contentType': 'COMM',
        'countryCode': '82',
        'from': f'01097590231',
        'to': [
            f'{phone_number}',
        ],
        'content': f'인증번호 [{auth_number}]'
    }

    requests.post(SMS_URL, headers=headers, json=data)



# Create your views here.
def find_user_view(request):
    if request.method == 'POST':
        user_info = request.POST.get('send-info', '')
        type_info = user_info.find('@')

        if type_info == -1:
            auth_num = randint(1000, 10000)
            exist_phone = UserModel.objects.filter(phone_number=user_info)
            model_phone = UserModel.objects.get(phone_number=user_info)
            exist_auth = AuthSms.objects.filter(phone_num=user_info)
            get_auth = AuthSms.objects.get(phone_num=user_info)

            if exist_phone:
                if exist_auth:
                    get_auth.auth_number = auth_num
                    get_auth.save()
                else:
                    AuthSms.objects.create(phone_num=model_phone.phone_number, auth_number=auth_num)

                send_sms(phone_number=user_info, auth_number=auth_num)

                return render(request, 'find_pw/certi_num_page.html')
            else:
                return redirect('/find-pw')


        else:
            user = get_user_model().objects.filter(username = user_info)
            if user:
                current_site = get_current_site(request)
                message = render_to_string('find_pw/user_certification_mail.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)).encode().decode(),
                    'token': account_activation_token.make_token(user),
                })
                mail_title = "계정 활성화 확인 이메일"
                mail_to = request.POST["user_info"]
                email = EmailMessage(mail_title, message, to=[mail_to])
                email.send()

                return render(request,'find_pw/certi_num_page.html')
    elif request.method == 'GET':
        return render(request, 'find_pw/find_pw_page.html')


def certi_num_view(request):
    return render(request,'find_pw/certi_num_page.html')

def set_pw_view(request):
    return render(request,'find_pw/set_pw_page.html')