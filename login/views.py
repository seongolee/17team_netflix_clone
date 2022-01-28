from django.shortcuts import render, redirect
from user.models import UserModel   #아마 사인업의 모델스.파이 에서 유저 데이터 쌓는 클래스가 있을건데 거기서 가져올듯
from django.http import HttpResponse
from django.contrib.auth import get_user_model # 사용자가 데이터베이스 안에 있는지 검사하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_view(request):
    # if request.method == 'POST':
    #     # 아래 유저네임과 패스워드는 연결 된 html 파일 내부에 'name:  ' 과 같아야 함
    #     # db에 저장된 아이디랑 패스워드 맞는지 확인해야하고, 핸드폰 번호랑 이메일 둘다 아이디로 쓰게 추가설정해야함.
    #     username = request.POST.get('username', None)
    #     password = request.POST.get('password', None)
    #
    #
    #
    #     me = auth.authenticate(request, username=username, password=password)
    #     # 주황색은 유저모델에 있는 유저네임 값이고, 옆에는 디비와 일치하는 사용자 이름
    #     # me = UserModel.objects.get(username=username)
    #
    #     # user = request.user.is_authenticated #로그인한 상태의 유저가 담겨있음.    --->>> 성오님 추가 설명 해주신다함 220128
    #
    #     # 유저가 맞으면 로그인해서 main 뷰스에서 메인으로 보내주는 기본 패스로 연결 아니면 로그인페이지로
    #     if me is not None:
    #         auth.login(request, me)
    #         # request.session['user'] = me.username
    #         return redirect('/')
    #     else:
    #         return render(request,'login/login_page.html')
    return render(request,'login/login_page.html')
        # return HttpResponse(me.username)

#     # 로그인된 사용자는 로그인 페이지 잘못 쳐도 메인페이지로 보내주게 예외처리
#     elif request.method == 'GET':
#         user = request.user.is_authenticated
#         if user:
#             redirect('/')
#         else:
#             return render(request, 'user/signin.html')
#
# # @login_required             # 사용자가 로그인이 꼭 되어있어야만 접근이 가능한 함수라는 뜻
# def login(request):
#
#     return render(request, 'mainpage_html/main.html')