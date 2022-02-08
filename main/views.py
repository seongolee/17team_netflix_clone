from django.shortcuts import render, redirect
from login.views import login_required
from django.contrib import auth
from .models import Video, VideoModal, Genre
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


def search(request):
    return render(request, 'mainpage_html/search.html')


from main.models import Video
from django.http import JsonResponse
from django.views import View

# # 장고 검색기능 구현
# class SearchView(View):
#     def get(self, request):
#         try:
#             word = request.GET.get('word', '')
#             results = []
#
#             ko_name = Video.objects.filter(korean_name__icontains=word).exists()
#             en_name = Video.objects.filter(english_name__icontains=word).exists()
#             # category_name = Category.objects.filter(name__icontains=word).exists()
#
#             if ko_name:
#                 videos = Video.objects.filter(korean_name__icontains=word)
#                 for video in videos:
#                     results.append({
#                         'word': video.korean_name
#                     })
#
#             if en_name:
#                 videos = Video.objects.filter(english_name__icontains=word)
#                 for video in videos:
#                     results.append({
#                         'word': video.english_name
#                     })
#
#             # if category_name:
#             #     categories = Category.objects.filter(name__icontains=word)
#             #     for category in categories:
#             #         results.append({
#             #             'word': category.name
#             #         })
#
#             return JsonResponse({'results': results}, status=201)
#
#         except Exception as error:
#             return JsonResponse({'message': error}, status=400)
#
#
# # like 해당하는 제목찾아서 그 제목의 like 쌓는 기능
# # 좋아요 기능 구현  POST 방식
# def like_star():
#     title_receive = request.form['title_give']
#     target_prodct = Video.objects.get({'title':title_receive})
#     current_prodct = target_prodct['like']
#     new_like = current_prodct + 1
#
#     db.crawling.update_one({'title': title_receive}, {'$set': {'like' : new_like}})
#     return jsonify({'msg': 'like!'})
#
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
    video = Video.objects.all()
    explain = VideoModal.objects.all()
    for i in range(6):
        video_title.append(video[i].video_title)
        video_image.append(video[i].video_image)
        video_explain.append(explain[i].video_description)

    #별점 순
    star_title = []
    star_image = []
    star_explain = []
    stars = Video.objects.all().order_by('-star_point')
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
    context = {'video_title': video_title ,
               'video_image':video_image,
               'explain':video_explain,
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


#모델 부분
import pandas as pd
import numpy as np
from .models import Recommendation
def predict(request):
    movie_ratings = Recommendation.objects.all().values()
    data = pd.DataFrame(movie_ratings)