"""JOININ2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from user.views import userlogin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$',userlogin),
    url(r'^user/',include("user.urls")),
    url(r'^student/',include("student.urls")),
    url(r'^system/',include("system.urls")),
    url(r'^school/',include("school.urls")),
    url(r'^department/',include("department.urls")),
    url(r'^major/',include("major.urls")),
    url(r'^clazz/',include("clazz.urls")),
    url(r'^schoolAdmin/', include("schoolAdmin.urls")),
    url(r'^communication/',include("communication.urls")),
    url(r'^image/',include("image.urls")),
    url(r'^organize/',include("organize.urls")),
    url(r'^organizeDepart/',include("organizeDepart.urls")),
    url(r'^associateInfo/',include("associateInfo.urls")),
]
