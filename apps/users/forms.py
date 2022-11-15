# -*- coding: utf-8 -*-
# @Time    : 2022/10/27 07:01
# @Author  : tianpeng
# @FileName: forms.py

from django import forms
from django.conf import settings
from captcha.fields import CaptchaField
import redis

from apps.users.models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=2)
    password = forms.CharField(required=True, min_length=3)


class DynamicLoginForm(forms.Form):
    mobile = forms.EmailField(required=True)
    captcha = CaptchaField()


class DynamicLoginPostForm(forms.Form):
    mobile = forms.EmailField(required=True)
    code = forms.CharField(required=True, min_length=6, max_length=6)

    def clean_code(self):
        email = self.data.get("mobile")
        code = self.data.get("code")
        r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0, charset="utf8", decode_responses=True)
        redis_code = r.get(email)
        print(redis_code)
        if code != redis_code:
            raise forms.ValidationError("验证码错误")
        else:
            return self.cleaned_data


class RegisterForm(forms.Form):
    mobile = forms.EmailField(required=True)
    code = forms.CharField(required=True, min_length=6, max_length=6)
    password = forms.CharField(required=True, min_length=6, max_length=20)

    def clean_mobile(self):
        mobile = self.data.get("mobile")
        user = UserProfile.objects.filter(email=mobile)
        if user:
            raise forms.ValidationError("用户已注册")
        else:
            return mobile

    def clean_code(self):
        email = self.data.get("mobile")
        code = self.data.get("code")
        r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0, charset="utf8", decode_responses=True)
        redis_code = r.get(email)
        if code != redis_code:
            raise forms.ValidationError("验证码错误")
        else:
            return code
