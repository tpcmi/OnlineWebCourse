# -*- coding: utf-8 -*-
# @Time    : 2022/10/19 08:33
# @Author  : tianpeng
# @FileName: adminx.py
import xadmin

from apps.operations.models import UserConsult, CourseComments, UserFav, UserMessage, UserCourse


class UserConsultAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'is_read', 'add_time']
    search_fields = ['user', 'message', 'is_read']
    list_filter = ['user', 'message', 'is_read', 'add_time']


class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user', 'course', 'comments', 'add_time']


class UserFavAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


xadmin.site.register(UserConsult, UserConsultAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFav, UserFavAdmin)
