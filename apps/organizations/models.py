from django.db import models

from apps.users.models import BaseModel

CATEGORY_CHOICES = (
    ("1", "培训机构"),
    ("2", "个人"),
    ("3", "高校")
)


class CourseOrg(BaseModel):
    name = models.CharField(verbose_name="机构名称", max_length=50)
    desc = models.TextField(verbose_name="描述")
    tag = models.CharField(verbose_name="机构标签", max_length=30, default="全国知名")
    category = models.CharField(verbose_name="机构类别", max_length=1, choices=CATEGORY_CHOICES)
    click_nums = models.IntegerField(verbose_name="点击数", default=0)
    fav_nums = models.IntegerField(verbose_name="收藏数", default=0)
    logo = models.ImageField(verbose_name="logo", upload_to="CourseOrg/", max_length=100)

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name
