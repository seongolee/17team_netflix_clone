from django.shortcuts import render, redirect
from login.views import login_required
from django.contrib import auth
from .models import Video, VideoModal, Genre, Actor,Recommendation
from user.models import UserModel
from django.http import HttpResponse
import json
from django.core import serializers


# Create your views here.
def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/main')
    else:
        return redirect('/kr')


# main_view

def main_view(request):
    return render(request, 'mainpage_html/main.html')


@login_required
def logout(request):
    auth.logout(request)
    print('로그아웃 이상무')
    return redirect('/')


def search_page(request):
    return render(request, 'mainpage_html/search.html')


from main.models import Video
from django.http import JsonResponse
from django.views import View


# # 장고 검색기능 구현

def showvideo(request):
    video_title = []
    video_image = []
    # video_explain = []
    video_clip = []

    video = Video.objects.all()
    # explain = VideoModal.objects.all()
    print(video)
    for i in range(40):
        video_title.append(video[i].video_title)
        video_image.append(video[i].video_image)
        # video_explain.append(explain[i].video_description)
        video_clip.append(video[i].video_clip)

    print(video_clip)
    print('success')
    print(video_image)
    context = {'video_title': video_title,
               'video_image': video_image,
               # 'explain':video_explain,
               'video_clip': video_clip}
    return HttpResponse(json.dumps(context), content_type="application/json")


# like 해당하는 제목찾아서 그 제목의 like 쌓는 기능
# 좋아요 기능 구현  POST 방식
# def like_star():
#     title_receive = request.form['title_give']
#     target_prodct = Video.objects.get({'title':title_receive})
#     current_prodct = target_prodct['like']
#     new_like = current_prodct + 1
#     video.total_like = new_like
#
#     db.crawling.update_one({'title': title_receive}, {'$set': {'like' : new_like}})
#     return jsonify({'msg': 'like!'})

#
# # like 순으로 배열하는 기능  GET 방식
# def showHeart():
#     like_heart = list(db.crawling.find({}, {'_id': False}).sort('like', -1).limit(5))
#     return jsonify({'likes_heart': like_heart})
#
# # 클라이언트 쪽 좋아요 버튼 함수 실행시 채워주는 거
# # function likeheart() {
# #             alert('좋아요 완료!')
# #             let like = document.getElementById("like");
# #             like.style.fill = "#c1ff31";
# #         }
#
# ## 받아서 쫙 뿌려주기 기능  GET 방식
# def showColumn():
#     product = list(db.columns.find({}, {'_id': False}).limit(3))
#     return jsonify({'products': product})


def showColumn(request):
    video_title = []
    video_image = []
    video_explain = []
    #아이템 기반 협업필터링
    cosine_item = item_based_recommenation()
    print(cosine_item)
    for i in cosine_item:
        video = Video.objects.get(video_title=i)
        explain = VideoModal.objects.get(video_id=video)
        video_title.append(video.video_title)
        video_image.append(video.video_image)
        video_explain.append(explain.video_description)

    # 별점 순
    star_title = []
    star_image = []
    star_explain = []
    stars = Video.objects.all().order_by('-total_like')
    for i in range(8):
        star_title.append(stars[i].video_title)
        star_image.append(stars[i].video_image)
        explain = VideoModal.objects.get(video_id=stars[i].id)
        star_explain.append(explain.video_description)

    # 로맨스 장르
    romance_title = []
    romance_image = []
    romance_explain = []
    romances = Genre.objects.get(genre_name="로맨스").genre.all()
    for i in range(8):
        romance_title.append(romances[i].video_title)
        romance_image.append(romances[i].video_image)
        explain = VideoModal.objects.get(video_id=romances[i].id)
        romance_explain.append(explain.video_description)
    # 액션 장르
    action_title = []
    action_image = []
    action_explain = []
    actions = Genre.objects.get(genre_name="액션").genre.all()
    for i in range(8):
        action_title.append(actions[i].video_title)
        action_image.append(actions[i].video_image)
        explain = VideoModal.objects.get(video_id=actions[i].id)
        action_explain.append(explain.video_description)

    # 공포 장르
    horror_title = []
    horror_image = []
    horror_explain = []
    horrors = Genre.objects.get(genre_name="공포").genre.all()
    for i in range(len(horrors)):
        horror_title.append(horrors[i].video_title)
        horror_image.append(horrors[i].video_image)
        explain = VideoModal.objects.get(video_id=horrors[i].id)
        horror_explain.append(explain.video_description)

    # 코미디 장르
    comedy_title = []
    comedy_image = []
    comedy_explain = []
    comedys = Genre.objects.get(genre_name="코미디").genre.all()
    for i in range(8):
        comedy_title.append(comedys[i].video_title)
        comedy_image.append(comedys[i].video_image)
        explain = VideoModal.objects.get(video_id=comedys[i].id)
        comedy_explain.append(explain.video_description)

    # 판타지 장르
    fantasy_title = []
    fantasy_image = []
    fantasy_explain = []
    fantasys = Genre.objects.get(genre_name="판타지").genre.all()
    for i in range(8):
        fantasy_title.append(fantasys[i].video_title)
        fantasy_image.append(fantasys[i].video_image)
        explain = VideoModal.objects.get(video_id=fantasys[i].id)
        fantasy_explain.append(explain.video_description)

    print('success')
    print(star_title)
    context = {'video_title': video_title,
               'video_image': video_image,
               'explain': video_explain,
               'romance_title': romance_title,
               'romance_image': romance_image,
               'romance_explain': romance_explain,
               'horror_title': horror_title,
               'horror_image': horror_image,
               'horror_explain': horror_explain,
               'comedy_title': comedy_title,
               'comedy_image': comedy_image,
               'comedy_explain': comedy_explain,
               'action_title': action_title,
               'action_image': action_image,
               'action_explain': action_explain,
               'fantasy_title': fantasy_title,
               'fantasy_image': fantasy_image,
               'fantasy_explain': fantasy_explain,
               'star_title': star_title,
               'star_image': star_image,
               'star_explain': star_explain
               }
    return HttpResponse(json.dumps(context), content_type="application/json")



# 장고 검색기능 재도전!
def search(request):
    if request.method == 'GET':

        query = request.GET['query']

        title = Video.objects.filter(video_title__contains=query)
        actor = Actor.objects.filter(actor_name__contains=query)
        genre = Genre.objects.filter(genre_name__contains=query)
        if title:
            title = Video.objects.filter(video_title__contains=query)
        else:
            if actor:
                title = Actor.objects.get(actor_name__contains=query).actor.all()
            else:
                if genre:
                    title = Genre.objects.get(genre_name__contains=query).genre.all()
                else:
                    title = []

        # genre = Video.genre.all()
        # video = Video.objects.get(video_title__contains=query)
        # title = video.video_title
        # video_image = video.video_image(video_title=video_image[i].video_title)
        # video_clip = video.video_clip
        # genre = Genre.objects.filter(genre_name__contains=query)
        # selectmovie = title.union(genre)

        #
        # video = Video.objects.all()
        # explain = VideoModal.objects.all()
        # print(video)
        # for i in range(40):
        # video_title.append(video[i].video_title)
        # video_image.append(video[i].video_image)
        # video_explain.append(explain[i].video_description)
        # video_clip.append(video[i].video_clip)
        #
        # print(video_clip)
        # print('success')
        # print(video_image)
        context = {
            # 'selectmovie': selectmovie,
            "query": query,
            "title": title,

        }

        return render(request, 'mainpage_html/search.html', context)
    elif request.method == 'POST':
        return render(request, 'mainpage_html/search.html')
    #
    # else:
    #     return render(request, 'mainpage_html/search.html')


def modal(request):
    title = request.GET.get('title')
    video = Video.objects.get(video_title=title)
    description = VideoModal.objects.get(video_id=video.id)
    genre = video.genre.all()
    actor = video.actors.all()
    total_genre = ''
    total_actor = ''
    for gen in range(len(genre)):
        total_genre += genre[gen].genre_name + ','
    final_genre = total_genre[:-1]

    for act in range(len(actor)):
        total_actor += actor[act].actor_name + ','
    print(actor)
    final_actor = total_actor[:-1]
    context = {'video_title': video.video_title,
               'description': description.video_description,
               'genre': final_genre,
               'video_clip': video.video_clip,
               'actor': final_actor,
               'rating': video.age_limit_logo

               }
    return HttpResponse(json.dumps(context), content_type="application/json")

import csv
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


ratings = pd.read_csv('static/recommendation/ratings.csv', encoding='cp949')
movies = pd.read_csv('static/recommendation/movies.csv', encoding='cp949')

# 데이터프레임을 출력했을때 더 많은 열이 보이도록 함
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 300)
# movieId를 기준으로 ratings 와 movies 를 결합함
movie_ratings = pd.merge(ratings, movies, on='movieId')



def item_based_recommenation():
    user_title = movie_ratings.pivot_table('rating', index='title', columns='userId')

    user_title = user_title.fillna(0)

    item_based_collab = cosine_similarity(user_title, user_title)

    item_based_collab = pd.DataFrame(item_based_collab, index=user_title.index, columns=user_title.index)

    collab = item_based_collab['불가살'].sort_values(ascending=False)[1:11].index
    # collab = item_based_collab['불가살'].values.tolist()
    # 불가살과 비슷하게 유저들로부터 평점을 부여받은 영화들은?

    return collab

def thumbs(request):
    print('소통')
    user = request.user
    users = UserModel.objects.get(email=user)
    print(users.id)
    title_give = request.POST.get('title_give')
    like = request.POST.get('final_like')
    video = Video.objects.get(video_title=title_give)

    Recommendation.objects.update_or_create(user_id=users,video_id=video,defaults={"thumbs":like})
    video.total_like += int(like)
    video.save()
    print(video.total_like)
    print(title_give)
    print(like)

    print('성공')

    context = {'count': '성공'}

    return HttpResponse(json.dumps(context), content_type="application/json")
