from django.db import models
from user.models import UserModel
# Create your models here.


# Genre 테이블
class Genre(models.Model):
    class Meta:
        db_table = "genre"

    # genre_name / 장르 이름
    genre_name = models.CharField(max_length=256)


class Video(models.Model):
    class Meta:
        db_table = "video"

    # genre / 장르
    genre = models.ManyToManyField('Genre', related_name='genre')

    actors = models.ManyToManyField('Actor', related_name='actor')

    creators = models.ManyToManyField('Creator', related_name='creator')

    video_title = models.CharField(max_length=256)
    # video_clip / 영상
    video_clip = models.URLField(max_length=256)
    # age_limit_logo / 관람등급
    age_limit_logo = models.CharField(max_length=256, default='')
    # star_point / 별점
    star_point = models.DecimalField(max_digits = 5, decimal_places = 3)
    # total_like / 전체 좋아요 수
    total_like = models.IntegerField(default=0)
    # total_views / 조회수
    total_views = models.IntegerField(default=0)
    # video_image / 썸네일
    video_image = models.CharField(max_length=1000)




# VideoModal 테이블
class VideoModal(models.Model):
    class Meta:
        db_table = "video_modal"

    # video_id / 비디오ID (채번값부여된)
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE, db_column='video_id')
    # # how_many_seasons / 시리즈 수
    # how_many_seasons = models.CharField(max_length=256)
    # video_description / 영상 소개
    video_description = models.CharField(max_length=10000)


# Actors 테이블
# class Actors(models.Model):
#     class Meta:
#         db_table = "actors"
#
#     # actor_id / 배우 ID # id 값으로 대체
#
#     # video_id / 비디오ID (채번값부여된)
#     video_id = models.ForeignKey(Video, on_delete=models.CASCADE, db_column='video_id')
#     actor_name = models.CharField(max_length=256)


# Actor 테이블
class Actor(models.Model):
    class Meta:
        db_table = "actor"

    # # actor_id / 배우 ID
    # actor_id = models.ForeignKey(Actors, on_delete=models.CASCADE, db_column='actor_id')
    # actor_name / 한국어 배우이름
    actor_name = models.CharField(max_length=256)


# # Creators 테이블
# class Creators(models.Model):
#     class Meta:
#         db_table = "creators"
#
#     # creators_id / 감독 ID # id 값으로 대체
#
#     # video_id / 비디오ID (채번값부여된)
#     video_id = models.ForeignKey(Video, on_delete=models.CASCADE, db_column='video_id')


# Creator 테이블
class Creator(models.Model):
    class Meta:
        db_table = "creator"

    # # creator_id / 감독 ID
    # creator_id = models.ForeignKey(Creators, on_delete=models.CASCADE, db_column='creator_id')
    # creator_name / 감독 이름
    creator_name = models.CharField(max_length=256)


# Recommendation 테이블
class Recommendation(models.Model):
    class Meta:
        db_table = "recommendation"

    # profile_id
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE, db_column='user_id')
    # video_id / 비디오ID (채번값부여된)
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE, db_column='video_id')
    # thumbs / 좋아요 or 싫어요
    thumbs = models.BooleanField(null=True)
    # my_list_or_not / 찜
    my_list_or_not = models.BooleanField(null=True)
    # streaming_info / 영상재생시간
    streaming_info = models.CharField(max_length=256, default='0s')
    # star_info / 별점
    star_info = models.CharField(max_length=256, default='0')