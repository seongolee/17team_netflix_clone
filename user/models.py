from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "UserModel"

    # bio = models.CharField(max_length=256, default='')  # 상태메세지
    # follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followee')


    phone_number = models.CharField(max_length=30, blank=False)
    country_code = models.CharField(max_length=256, default='ko')


class ProfileId(models.Model):
    class Meta:
        db_table = "ProfileId"

    profile_id =  models.CharField(max_length=256, blank=False)
    profile_name = models.CharField(max_length=256, blank=False)
    # bookimages = models.ImageField(upload_to='static/bookimages',default='None.jpg')
    profile_image = models.ImageField(upload_to='', default='')
    profile_can_use = models.BooleanField(default=True)
    kids_or_not = models.BooleanField(default=False)


