from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.conf import settings


# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "user_model"

    email = models.EmailField(verbose_name="email", max_length=255, unique=True)
    username = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30, unique=True)
    country_code = models.CharField(max_length=256, default='ko')

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



class ProfileId(models.Model):
    class Meta:
        db_table = "profile_id"

    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE, db_column='user_id')
    profile_id = models.AutoField(primary_key=True)
    profile_name = models.CharField(max_length=256, )
    # profile_image = models.ImageField(upload_to='static/bookimages',default='None.jpg')
    profile_image = models.ImageField(upload_to='', default='')
    profile_can_use = models.BooleanField(default=True)
    kids_or_not = models.BooleanField(default=False)


class FooterInfo(models.Model):
    class Meta:
        db_table = "footer_info"

    # 법인이름
    company_name = models.CharField(max_length=256)
    # 통신판매업신고번호
    report_number = models.CharField(max_length=256)
    # 전화번호
    company_number = models.CharField(max_length=256)
    # 대표이름
    Representative_name = models.CharField(max_length=256)
    # 이메일주소
    company_email = models.CharField(max_length=256)
    # 법인주소지
    company_address = models.CharField(max_length=256)
    # 사업자등록번호
    Business_number = models.CharField(max_length=256)



# # 전화번호인증 관련 모델
class AuthSms(models.Model):
    class Meta:
        db_table = 'auth_numbers'

    phone_number = models.CharField(max_length=256)
    auth_number = models.IntegerField()


