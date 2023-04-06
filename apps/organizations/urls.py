# -*- coding: utf-8 -*-
# @Time    : 2023/3/3 07:36
# @Author  : tianpeng
# @FileName: urls
from django.urls import path

from apps.organizations.views import OrgView, UserConsultView, OrgHomeView

urlpatterns = [
    path('list/', OrgView.as_view(), name="list"),
    path('add_ask/', UserConsultView.as_view(), name="add_ask"),
    path('<int:org_id>/', OrgHomeView.as_view(), name="home")
]
