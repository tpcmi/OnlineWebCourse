# Generated by Django 3.2.10 on 2022-10-13 03:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseOrg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=50, verbose_name='机构名称')),
                ('desc', models.TextField(verbose_name='描述')),
                ('tag', models.CharField(default='全国知名', max_length=30, verbose_name='机构标签')),
                ('category', models.CharField(choices=[('1', '培训机构'), ('2', '个人'), ('3', '高校')], max_length=4, verbose_name='机构类别')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏数')),
                ('logo', models.ImageField(upload_to='CourseOrg/<django.db.models.fields.CharField>/', verbose_name='logo')),
            ],
            options={
                'verbose_name': '课程机构',
                'verbose_name_plural': '课程机构',
            },
        ),
    ]
