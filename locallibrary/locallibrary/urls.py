"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path
from django.urls import include

# 开启用户系统
urlpatterns = [
    path('admin/', admin.site.urls)
]

# 开启 catalog 模块
urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/')),
]

# 配置静态文件
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# 用户登录模块
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
