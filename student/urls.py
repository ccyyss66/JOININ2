from django.conf.urls import url
from student.views import *

urlpatterns = [
    url(r'^studentIndex/',studentIndex),
    url(r'^personalInfo/',personalInfo),
    url(r'^publishinformation/',publishinformation),
    url(r'^viewinformation/',viewinformation),
    url(r'^addInformation/',addInformation),
    url(r'^associateInfo/',associateinfo),
    # # url(r'^findOneByUserId/',findOneByUserId),
    url(r'^findStudentInfoDetail/',findStudentInfoDetailByUserId),
    url(r'^modifyStudentInfoDetail/',modifyStudentInfoDetail),
]