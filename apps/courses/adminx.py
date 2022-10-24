# -*- coding: utf-8 -*-
# @Time    : 2022/10/18 09:42
# @Author  : tianpeng
# @FileName: adminx
import xadmin
from xadmin.views import CommAdminView, BaseAdminView

from apps.courses.models import Course, Lesson, Video, CourseResource


class GlobalSettings(object):
    site_title = "网课后台管理系统"
    site_footer = "tpcmi在线网课"
    # menu_style = "accordion"


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class CourseAdmin:
    list_display = ['name', 'desc', 'detail', 'degree', 'learning_duration', 'students']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    list_filter = ['name', 'teacher__name', 'desc', 'detail', 'degree', 'learning_duration', 'students']
    list_editable = ["degree", "desc"]


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'file', 'add_time']
    search_fields = ['course', 'name', 'file']
    list_filter = ['course', 'name', 'file', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(CommAdminView, GlobalSettings)
xadmin.site.register(BaseAdminView, BaseSettings)
