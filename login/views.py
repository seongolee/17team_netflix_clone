from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from user.models import UserModel



# Create your views here.
def login_view(request):
    if request.method == 'POST':
        # 아래 유저네임과 패스워드는 연결 된 html 파일 내부에 'name:  ' 과 같아야 함
        user_email = request.POST.get('username', None)
        password = request.POST.get('password', None)

        temp = user_email.find('@')
        # 위의 find 결과값이 @가 있으면 1 없으면 -1이 반환 됨. 그래서 -1이면 폰번호이므로 폰번호와 매칭시켜 해당하는 email값을 반환
        if temp == -1:
            correct_id = UserModel.objects.filter(phone_number=user_email).values('email')

            if correct_id:
                user_email = list(correct_id)[0]['email']
            else:
                return redirect('/login')
            # get --->>>  filter로 수정보완 요망 / get로 받으면 입력값이 없을 때 오류가 나고 리다이렉트 페이지 반환이 안 되기 때문임
            # user_email = list(UserModel.objects.filter(phone_number=user_email).values('email'))[0]['email']
        # 유저네임뿐 아니라 폰넘버로도 로그인 가능하게 할 예정
        # phone_number = request.POST.get('phone_number', None)

        # me = auth.authenticate(request, username=username, password=password)

        # 겟으로 가져온 게 오른쪽 / 왼쪽에 있는 게 db
        me_username = auth.authenticate(request, email=user_email, password=password)
        print(me_username)
        print('유저네임 로그인 권한 받았습니다')
        # me_phone_number = auth.authenticate(request, phone_number=user_phone, password=password)
        # print('로그인 권한 받았습니다')
        # 주황색은 유저모델에 있는 유저네임 값이고, 옆에는 디비와 일치하는 사용자 이름
        # me = UserModel.objects.get(username=username)

        if me_username is not None:
            auth.login(request, me_username)
            print('이메일 로그인 인증')
            # auth.login(request, me)
            # request.session['user'] = me.username
            return redirect('/login/profile')

        else:
            print('로그인 리다이렉트')
            return redirect('/login')

        # return HttpResponse(me.username)


    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/main')
            print('너 로그인 사용자 메인으로 ㄱㄱ')

        else:
            print('로그인부터 해라')
            return render(request, 'login/login_page.html')


# @login_required
# def logout(request):
#     auth.logout(request)
#     return redirect('/')

# 카카오 로그인 연동
import requests
import json
from django.template import loader
from django.http import HttpResponse, JsonResponse


def index(request):
    _context = {'check':False}
    if request.session.get('access_token'):
        _context['check'] = True
    return render(request, 'sign_up_check.html', _context)
def kakaoLoginLogic(request):
    _restApi = secrets['KAKAO']['RESTAPI']
    _redirectUrl = 'http://127.0.0.1:8000/login/profile/'
    _url = f'https://kauth.kakao.com/oauth/authorize?client_id={_restApi}&redirect_uri={_redirectUrl}&response_type=code'
    return redirect(_url)
def kakaoLoginLogicRedirect(request):
    _qs = request.GET['code']
    _restApi = secrets['KAKAO']['RESTAPI']
    _redirect_uri = 'http://127.0.0.1:8000/login/profile/'
    _url = f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={_restApi}&redirect_uri={_redirect_uri}&code={_qs}'
    _res = requests.post(_url)
    _result = _res.json()
    request.session['access_token'] = _result['access_token']
    request.session.modified = True
    return render(request, 'login/profile.html')
def kakaoLogout(request):
    _token = request.session['access_token']
    _url = 'https://kapi.kakao.com/v1/user/logout'
    _header = {
      'Authorization': f'bearer {_token}'
    }
    # _url = 'https://kapi.kakao.com/v1/user/unlink'
    # _header = {
    #   'Authorization': f'bearer {_token}',
    # }
    _res = requests.post(_url, headers=_header)
    _result = _res.json()
    if _result.get('id'):
        del request.session['access_token']
        return render(request, 'logout_page.html')
    else:
        return render(request, 'logoutError.html')

def profile(request):
    return render(request, 'login/profile.html')