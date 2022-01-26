from django.shortcuts import render
from user.models import UserModel, ProfileId
from main.models import Genre, Video, VideoModal


# Create your views here.
def sign_up(request):
    # user = UserModel.objects.create_user(username='test10', password='test', email='test@gmail.com')
    #
    # for i in range(5):
    #     profile_id = str(user.id * 10) + str(i)
    #     ProfileId.objects.create(author=user, profile_id=profile_id, profile_name='test')
    genre = Genre.objects.create(genre_name='개발중...')

    temp_video = Video.objects.create(genre_id=genre, video_title='title', video_clip='https://', series_section='1시즌',
                                      star_point='5', total_like='5', total_views='5')

    VideoModal.objects.create(video_id=temp_video, how_many_seasons='1화', video_description='1화소개')
    VideoModal.objects.create(video_id=temp_video, how_many_seasons='2화', video_description='2화소개')
    return render(request, 'sign_up/sign_up.html')
