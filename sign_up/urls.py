from django.urls import path
from . import views


urlpatterns = [
    path('', views.sign_up_check, name='sign_up_check')
]
