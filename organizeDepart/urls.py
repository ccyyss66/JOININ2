from django.conf.urls import url
from organizeDepart.views import *

urlpatterns = [
    url(r'^addOne/', addOne),
    url(r'^findByOrganizeid/',findByOrganizeid),
    # url(r'^modifyOneById/',modifyOneById),
    url(r'^deleteOneById/',deleteOneById)
]