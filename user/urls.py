from django.conf.urls import url
from user.views import *

urlpatterns = [
    url(r'^login/', login),
    url(r'^register/', register),
    url(r'^userlogin', userlogin),
    url(r'^logout/',logout),
    url(r'^userRegister/', userRegister),
    url(r'findOneDetailById/', findOneDetailById),
    url(r'^addOneChairman/',addOneChairman),
]