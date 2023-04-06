# -*- coding: utf-8 -*-
# @Time    : 2023/3/3 23:22
# @Author  : tianpeng
# @FileName: forms
import re

from django import forms

from apps.operations.models import UserConsult


class UserConsultModelForm(forms.ModelForm):
    mobile = forms.CharField(max_length=11, min_length=11, required=True)

    class Meta:
        model = UserConsult
        fields = ["name", "mobile", "course_name"]

    def clean_mobile(self):
        """
        验证手机号是否合法
        """
        mobile = self.cleaned_data["mobile"]
        regex_mobile = "^(13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8}$"
        p = re.compile(regex_mobile)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError("手机号非法!")
