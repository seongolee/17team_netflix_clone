from django.urls import path
from . import views

urlpatterns = [
    path('', views.find_user_view, name='find-user'),
    path('certi/',views.certi_num_view, name='certi-num'),
    path('set-pw/',views.set_pw_view, name='set-pw'),

]