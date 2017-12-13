from django.conf.urls import url
from clazz.views import *

urlpatterns = [
    url(r'^addOne/',addOne),
    url(r'^findByMajorId/',findByMajorId),
    # url(r'^/',),
]