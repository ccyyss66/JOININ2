from django.conf.urls import url
from major.views import *

urlpatterns = [
    url(r'^addOne/',addOne),
    url(r'^findByDepartmentId/',findByDepartmentId),
    # url(r'^/',),
]