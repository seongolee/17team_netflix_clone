from django.urls import path
from . import views

urlpatterns = [
    path('find-user/', views.find_user_view, name='find-user'),
]