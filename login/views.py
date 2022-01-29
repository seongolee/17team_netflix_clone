
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):

    if request.method == 'POST':
        # 아래 유저네임과 패스워드는 연결 된 html 파일 내부에 'name:  ' 과 같아야 함
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        phonenumber = request.POST.get('phonenumber', None)

        # 유저네임뿐 아니라 폰넘버로도 로그인 가능하게 할 예정
        # phone_number = request.POST.get('phone_number', None)

        # me = auth.authenticate(request, username=username, password=password)

        me_username = auth.authenticate(request, username=username , password=password)
        me_phonenumber = auth.authenticate(request, phonenumber=phonenumber, password=password)
        # 주황색은 유저모델에 있는 유저네임 값이고, 옆에는 디비와 일치하는 사용자 이름
        # me = UserModel.objects.get(username=username)

        if me_username or me_phonenumber is not None:

            auth.login(request, me_username)
            print('이메일 로그인 인증')
            auth.login(request, me_phonenumber)
            print('폰번호 로그인 인증')
            # request.session['user'] = me.username
            request.session['user'] = me_username.username
            request.session['user'] = me_phonenumber.username
            return redirect('/main')
            print('main')
        else:

            return redirect('/login')
            print('로그인 리다이렉트')
        # return HttpResponse(me.username)


    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            redirect('/main')
            print('너 로그인 사용자 메인으로 ㄱㄱ')
        else:
            return render(request,'login/login_page.html')
            print('로그인부터 해라')

# # 깃헙 로그인
# from django.shortcuts import redirect, reverse
# from django.contrib import messages
#
# def github_login(request):
#     try:
#         if request.user.is_authenticated:
#             raise SocialLoginException("User already logged in")
#         client_id = os.environ.get("GH_ID")
#         redirect_uri = "http://127.0.0.1:8000/main"
#         scope = "read:user"
#         return redirect("https://github.com/login/oauth/authorize?client_id=20e584be6cc07419e4ca&redirect_uri=http://127.0.0.1:8000/main")
#     except SocialLoginException as error:
#         messages.error(request, error)
#         return redirect("core:home")

# def github_login_callback(request):
#     try:
#         if request.user.is_authenticated:
#             raise SocialLoginException("User already logged in")
#         code = request.GET.get("code", None)
#         if code is None:
#             raise GithubException("Can't get code")
#
#         client_id = os.environ.get("GH_ID")
#         client_secret = os.environ.get("GH_SECRET")
#
#         token_request = requests.post(
#             f"https://github.com/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}&code={code}",
#             headers={"Accept": "application/json"},
#         )
#         token_json = token_request.json()
#         error = token_json.get("error", None)
#
#         if error is not None:
#             raise GithubException("Can't get access token")

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')