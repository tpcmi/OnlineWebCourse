from django.db import models

from apps.users.models import BaseModel
from apps.organizations.models import Teacher, CourseOrg

COURSE_DEGREE_CHOICES = (
    ("1", "初级"),
    ("2", "中级"),
    ("3", "高级")
)


class Course(BaseModel):
    name = models.CharField(verbose_name="课程名", max_length=50)
    desc = models.CharField(verbose_name="课程描述", max_length=300)
    learning_duration = models.IntegerField(verbose_name="学习时长(分钟)", default=0)
    degree = models.CharField(verbose_name="难度", max_length=1, choices=COURSE_DEGREE_CHOICES)
    students = models.IntegerField(verbose_name="学习人数", default=0)
    fav_nums = models.IntegerField(verbose_name="收藏人数", default=0)
    click_nums = models.IntegerField(verbose_name="点击数", default=0),
    category = models.CharField(verbose_name="课程类别", max_length=50, default="后端开发")
    tag = models.CharField(verbose_name="课程标签", max_length=50, default="")
    instructions = models.CharField(verbose_name="课程须知", max_length=300, default="")
    teacher_words = models.CharField(verbose_name="教师嘱咐", max_length=300, default="")
    detail = models.TextField(verbose_name="课程详情")
    cover = models.ImageField(verbose_name="封面图", upload_to="courses", max_length=100)
    teacher = models.ForeignKey(Teacher, verbose_name="教师", on_delete=models.CASCADE, default=1)
    course_org = models.ForeignKey(CourseOrg, verbose_name="所属机构", on_delete=models.CASCADE, blank=True, null=True)
    is_classic = models.BooleanField(verbose_name="是否为经典课程", default=False)

    class Meta:
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="章节名", max_length=100)
    learning_duration = models.IntegerField(verbose_name="学习时长(分钟)", default=0)

    class Meta:
        verbose_name = "课程章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="视频名", max_length=100)
    learning_duration = models.IntegerField(verbose_name="学习时长(分钟)", default=0)
    url = models.URLField(verbose_name="视频地址", max_length=200)

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="资源名", max_length=100)
    file = models.FileField(verbose_name="下载地址", upload_to=f"course/resource/{course.name}", max_length=200)

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
