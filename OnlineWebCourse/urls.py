"""OnlineWebCourse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
import xadmin

from apps.users.views import LoginView, LogoutView, RegisterView, SendSmsView, DynamicLoginView
from apps.organizations.views import OrgView

import apps.organizations.views

urlpatterns = [
                  path('', TemplateView.as_view(template_name='index.html'), name="index"),
                  path('login/', LoginView.as_view(), name="login"),
                  path('d_login/', DynamicLoginView.as_view(), name="d_login"),
                  path('logout/', LogoutView.as_view(), name="logout"),
                  path('register/', RegisterView.as_view(), name="register"),
                  path('send_sms/', csrf_exempt(SendSmsView.as_view()), name='send_sms'),
                  path('xadmin/', xadmin.site.urls),
                  path('captcha/', include('captcha.urls')),
                  path('org/', include(("apps.organizations.urls", "organizations"), namespace="org")),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
