"""DemoTestYXB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from vvv1 import views

# 总路由
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.index_view),           # 访问 :  http://localhost:8866/hello/
    path('page/', views.V_web),                 # 访问 :  http://localhost:8866/page/
    path('test001/', include('vvv1.urls')),     # 跳转到子路由 访问 http://localhost:8866/test001/

]

