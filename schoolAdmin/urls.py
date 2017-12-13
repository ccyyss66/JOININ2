from django.conf.urls import url
from schoolAdmin.views import *

urlpatterns = [
    url(r'^index/',index),
    url(r'^personalInfo/',personalInfo),
    url(r'^findDepartmentMajorClassDetailBySchoolId/',findDepartmentMajorClassDetailBySchoolId),
    url(r'^findSchoolAdminDetail/',findSchoolAdminDetailById),
    url(r'^departmentAndMajorAndClass/',departmentAndMajorAndClass),
    url(r'^addDepartment/',addDepartment),
    url(r'^addMajor/',addMajor),
    url(r'^addClass',addClass),
    url(r'^communication/', communication),
    url(r'^organized/',organized),
    url(r'^addOneSchoolAdmin/',addOneSchoolAdmin),
    url(r'^organized/',organized),
    url(r'^viewMates/(.+)/$',viewmates),
    url(r'^depart/(.+)/$',depart)
]