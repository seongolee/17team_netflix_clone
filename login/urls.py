from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    # 카카오로그인 설정
    path('', views.index, name='kakao'),
    path('kakaoLoginLogic/', views.kakaoLoginLogic),
    path('kakaoLoginLogicRedirect/', views.kakaoLoginLogicRedirect),
    path('kakaoLogout/', views.kakaoLogout),

]
