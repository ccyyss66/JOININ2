from django.conf.urls import url
from department.views import *

urlpatterns = [
    url(r'^addOne/',addOne),
    url(r'^findBySchoolId/',findBySchoolId),
    # url(r'^/',),
]