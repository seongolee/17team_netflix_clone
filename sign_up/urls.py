from django.urls import path
from . import views


urlpatterns = [
    path('kr/', views.sign_up, name='sign_up')
]
