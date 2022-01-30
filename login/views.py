from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from user.models import UserModel


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        # 아래 유저네임과 패스워드는 연결 된 html 파일 내부에 'name:  ' 과 같아야 함
        user_email = request.POST.get('username', None)
        print(user_email)
        password = request.POST.get('password', None)

        user_phone = UserModel.objects.get(phone_number=user_email).email
        print(user_phone)

        # 유저네임뿐 아니라 폰넘버로도 로그인 가능하게 할 예정
        # phone_number = request.POST.get('phone_number', None)

        # me = auth.authenticate(request, username=username, password=password)

        # 겟으로 가져온 게 오른쪽 / 왼쪽에 있는 게 db
        me_username = auth.authenticate(request, email=user_email, password=password)
        print(me_username)
        print('유저네임 로그인 권한 받았습니다')
        me_phone_number = auth.authenticate(request, phone_number=user_phone, password=password)
        print('로그인 권한 받았습니다')
        print(me_phone_number)
        # 주황색은 유저모델에 있는 유저네임 값이고, 옆에는 디비와 일치하는 사용자 이름
        # me = UserModel.objects.get(username=username)

        if me_username or me_phone_number is not None:
            auth.login(request, me_username)
            print('이메일 로그인 인증')
            auth.login(request, me_phone_number)
            print('폰번호 로그인 인증')
            # auth.login(request, me)
            # request.session['user'] = me.username
            return redirect('/main')

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


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')
