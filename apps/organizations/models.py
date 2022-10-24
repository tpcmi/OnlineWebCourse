from django.db import models

from apps.users.models import BaseModel


class City(BaseModel):
    name = models.CharField(verbose_name="城市", max_length=20)
    desc = models.CharField(verbose_name="城市描述", max_length=200)

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


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
    address = models.CharField(verbose_name="地址", max_length=150, default="")
    students = models.IntegerField(verbose_name="学生人数", default=0)
    course_nums = models.IntegerField(verbose_name="课程数", default=0)
    city = models.ForeignKey(City, verbose_name="所在城市", on_delete=models.CASCADE, default="")

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(BaseModel):
    org = models.ForeignKey(CourseOrg, verbose_name="所属机构", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="教师名", max_length=50)
    work_years = models.IntegerField(verbose_name="工作年限", default=0)
    work_company = models.CharField(verbose_name="就职公司", max_length=50)
    work_position = models.CharField(verbose_name="公司职位", max_length=50)
    feature = models.CharField(verbose_name="教学特点", max_length=50)
    click_nums = models.IntegerField(verbose_name="点击数", default=0)
    fav_nums = models.IntegerField(verbose_name="收藏数", default=0)
    age = models.IntegerField(verbose_name="年龄", default=18)
    avatar = models.ImageField(verbose_name="头像", upload_to="teacher/", max_length=100)

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
