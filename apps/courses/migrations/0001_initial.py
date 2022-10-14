# Generated by Django 3.2.10 on 2022-10-13 03:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=50, verbose_name='课程名')),
                ('desc', models.CharField(max_length=300, verbose_name='课程描述')),
                ('learning_duration', models.IntegerField(default=0, verbose_name='学习时长(分钟)')),
                ('degree', models.CharField(choices=[(1, '初级'), (2, '中级'), (3, '高级')], max_length=1, verbose_name='难度')),
                ('students', models.IntegerField(default=0, verbose_name='学习人数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏人数')),
                ('category', models.CharField(default='后端开发', max_length=50, verbose_name='课程类别')),
                ('tag', models.CharField(default='', max_length=50, verbose_name='课程标签')),
                ('instructions', models.CharField(default='', max_length=300, verbose_name='课程须知')),
                ('teacher_words', models.CharField(default='', max_length=300, verbose_name='教师嘱咐')),
                ('detail', models.TextField(verbose_name='课程详情')),
                ('cover', models.ImageField(upload_to='courses', verbose_name='封面图')),
            ],
            options={
                'verbose_name': '课程信息',
                'verbose_name_plural': '课程信息',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=100, verbose_name='章节名')),
                ('learning_duration', models.IntegerField(default=0, verbose_name='学习时长(分钟)')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
            options={
                'verbose_name': '课程章节',
                'verbose_name_plural': '课程章节',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=100, verbose_name='视频名')),
                ('learning_duration', models.IntegerField(default=0, verbose_name='学习时长(分钟)')),
                ('url', models.URLField(verbose_name='视频地址')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.lesson')),
            ],
            options={
                'verbose_name': '视频',
                'verbose_name_plural': '视频',
            },
        ),
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=100, verbose_name='资源名')),
                ('file', models.FileField(max_length=200, upload_to='course/resource/None', verbose_name='下载地址')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
            options={
                'verbose_name': '课程资源',
                'verbose_name_plural': '课程资源',
            },
        ),
    ]