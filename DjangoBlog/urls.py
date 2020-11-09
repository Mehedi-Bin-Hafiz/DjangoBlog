"""DjangoBlog URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from posts.views import post_home,post_delete,post_list,post_detail,post_create,post_update
from .views import my_home

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^post/$",post_home,name='posthome'),
    url(r"^(?P<id>\d+)/$",post_detail, name='details'),
    url(r"^post_list/$",post_list),
    url(r"^post_create/$",post_create),
    url(r"^(?P<id>\d+)/edit/$",post_update,name='update'),
    url(r"^delete/$",post_home),
    url(r"",my_home,name='MyHome'),
]
