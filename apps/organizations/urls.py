# -*- coding: utf-8 -*-
# @Time    : 2023/3/3 07:36
# @Author  : tianpeng
# @FileName: urls
from django.urls import path

from apps.organizations.views import OrgView

urlpatterns = [
    path('list/', OrgView.as_view(), name="list")
]
