from django.conf.urls import url
from school.views import *

urlpatterns = [
    url(r'^addOne/',addOne),
    url(r'^findAll/',findAllSchool),
    url(r'^findByUniversityid/',findByUniversityid),
]