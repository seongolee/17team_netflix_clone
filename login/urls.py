from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    # 카카오로그인 설정
    path('', views.index, name='kakao'),
    path('test/', views.test),
    path('kakaoLoginLogic/', views.kakaoLoginLogic),
    path('kakaoLoginLogicRedirect/', views.kakaoLoginLogicRedirect),
    path('kakaoLogout/', views.kakaoLogout),
]
