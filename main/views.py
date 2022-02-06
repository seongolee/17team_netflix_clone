from django.shortcuts import render, redirect
from login.views import login_required
from django.contrib import auth
from .models import Video, VideoModal
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
    video_url = []
    video_explain = []
    video = Video.objects.all()
    explain = VideoModal.objects.all()
    print(video)
    for i in range(6):
        video_title.append(video[i].video_title)
        video_url.append(video[i].video_clip)
        video_explain.append(explain[i].video_description)

    print('success')
    print(video_url)
    context = {'video_title': video_title ,
               'video_url':video_url,
               'explain':video_explain}
    return HttpResponse(json.dumps(context), content_type="application/json")