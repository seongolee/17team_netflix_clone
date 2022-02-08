from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('main/', views.main_view, name='main'),
    path('search/', views.search, name='search'),
    path('show-col/', views.showColumn, name='show-col'),
    # path('show-genre/', views.show_genre, name='show-genre'),
    path('search_enter/', views.showvideo, name='search_enter'),
    path('search_page/', views.search_page, name='search_page'),
    path('modal/', views.modal, name='modal'),
]