from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
]

# from django.urls import path
# from . import views
#
# app_name = "logins"
#
# urlpatterns = [
#     path("login/github/", views.login_view, name="github-login"),
#     path(
#         "login/github/callback/",
#         views.github_login_callback,
#         name="github-callback",
#     )
# ]