from django.conf.urls import url
from organize.views import *

urlpatterns = [
    url(r'^addOne/', addOne),
    url(r'^findOneById/', findOneDetailById),
    url(r'^findByCondition/',findByCondition),
    url(r'^findByConditionBySt',findByConditionBySt),
    url(r'^modifyOneById/',modifyOneById),
    url(r'^deleteOneById/',deleteOneById)
]