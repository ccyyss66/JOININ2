from django.conf.urls import url
from system.views import *

urlpatterns = [
    url(r'^index/',index),
    url(r'^schoolManage/',schoolManage),
    url(r'^addSchool/',addSchool),
    url(r'^organize/',organize),
    url(r'^test/',test)
]