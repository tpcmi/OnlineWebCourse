from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)


GENDER_CHOICES = (
    ("male", "男"),
    ("female", "女")
)


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default="")
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(verbose_name="性别", choices=GENDER_CHOICES, max_length=6)
    address = models.CharField(max_length=100, verbose_name="地址", default="")
    mobile = models.CharField(max_length=11, unique=True, verbose_name="手机号")
    avatar = models.ImageField(upload_to="avatar", default="avatar/default.jpg")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.nick_name:
            return self.nick_name
        else:
            return self.username
