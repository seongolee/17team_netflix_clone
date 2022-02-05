from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('main/', views.main_view, name='main'),
    path('search/', views.search, name='search'),
    # path('search_enter/', views.SearchView, name='search_enter'),
]