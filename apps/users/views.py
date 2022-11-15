import random

from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse
from django.conf import settings
import redis

from apps.users.forms import LoginForm, DynamicLoginForm, DynamicLoginPostForm, RegisterForm
from apps.utils.mail import send_sms
from apps.users.models import UserProfile


class DynamicLoginView(View):
    def post(self, request):
        login_form = DynamicLoginPostForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data["mobile"]
            is_existed = UserProfile.objects.filter(email=email)
            if is_existed:
                user = is_existed[0]
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponseRedirect(reverse("register"))
        else:
            is_dynamic = True
            dlogin_form = DynamicLoginForm()
            return render(request, 'login.html', {"msg": "验证码错误",
                                                  "dlogin_form": dlogin_form,
                                                  "is_dynamic": is_dynamic})


class SendSmsView(View):
    def post(self, request):
        sms_form = DynamicLoginForm(request.POST)
        if sms_form.is_valid():
            email = sms_form.cleaned_data['mobile']
            code = random.randint(100000, 999999)
            status = send_sms(email, code)
            if status:
                r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0, charset="utf8",
                                decode_responses=True)
                r.set(email, code)
                r.expire(email, 300)
                return JsonResponse({"status": "success"})
            else:
                return JsonResponse({"msg": "重新发送"})
        else:
            res = {}
            for e, v in sms_form.errors.items():
                res[e] = v
            return JsonResponse(res)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))

        login_form = DynamicLoginForm()
        return render(request, 'login.html', {"login_form": login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            # 此处不使用model类UserProfile直接查询原因在于，密码得先加密再查询，扩展性不好
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                print(1)
                return render(request, 'login.html', {"msg": "用户名或密码错误"})
        else:
            return render(request, 'login.html', {"msg": "用户名或密码错误"})


class RegisterView(View):
    def get(self, request):
        login_form = DynamicLoginForm()
        return render(request, 'register.html', {"login_form": login_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = register_form.cleaned_data["mobile"]
            password = register_form.cleaned_data["password"]
            user = UserProfile(username=email)
            user.set_password(password)
            user.email = email
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            login_form = DynamicLoginForm()
            for k, v in register_form.errors.items():
                print(k, v)
            return render(request, 'register.html', {"login_form": login_form,
                                                     "register_form": register_form})
