from django.db import models


class User(models.Model):
    """
    phonenum	手机号
    nickname	昵称
    sex	性别
    birth_year	出生年
    birth_month	出生月
    birth_day	出生日
    avatar	个人形象
    location	常居地
    """
    phonenum = models.CharField(max_length=11, unique=True)
    nickname = models.CharField(max_length=32)
    sex = models.IntegerField(default=0)
    birth_yaer = models.IntegerField(default=2000)
    birth_mohth = models.IntegerField(default=1)
    birth_day = models.IntegerField(default=1)
    avatar = models.CharField(max_length=256)
    location = models.CharField(max_length=64)

    class Meta:
        db_table = 'users'
