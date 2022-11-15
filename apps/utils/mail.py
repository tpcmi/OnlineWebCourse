# -*- coding: utf-8 -*-
# @Time    : 2022/11/8 13:31
# @Author  : tianpeng
# @FileName: mail
from django.core.mail import send_mail


def send_sms(email: str, code: int):
    return send_mail(
        subject="tpxrx.com",
        message="Welcome to tpxrx.com. \n"
                + f"Here is your validate code:{code}",
        from_email="djangotest1@126.com",
        recipient_list=[email],
        fail_silently=False
    )
