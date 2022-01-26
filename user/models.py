from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "user_model"

    # bio = models.CharField(max_length=256, default='')  # 상태메세지
    # follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followee')


    phone_number = models.CharField(max_length=30, default='')
    country_code = models.CharField(max_length=256, default='ko')


class ProfileId(models.Model):
    class Meta:
        db_table = "profile_id"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)


    profile_id = models.CharField(max_length=256)
    profile_name = models.CharField(max_length=256)
    # bookimages = models.ImageField(upload_to='static/bookimages',default='None.jpg')
    profile_image = models.ImageField(upload_to='', default='')
    profile_can_use = models.BooleanField(default=True)
    kids_or_not = models.BooleanField(default=False)



class Video(models.Model):
    class Meta:
        db_table = "profile_id"

    profile_id =  models.CharField(max_length=256)
    profile_name = models.CharField(max_length=256)
    # bookimages = models.ImageField(upload_to='static/bookimages',default='None.jpg')
    profile_image = models.ImageField(upload_to='', default='')
    profile_can_use = models.BooleanField(default=True)
    kids_or_not = models.BooleanField(default=False)

