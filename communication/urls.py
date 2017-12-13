from django.conf.urls import url
from communication.views import *

urlpatterns = [
    url(r'^addOne/' ,addOne),
    url(r'^findOneDetailById/', findOneDetailById),
    url(r'^findListByUserId/', findListByUserId),
    url(r'^findByCondition/', findByCondition),
    url(r'^deleteById/', deleteById),
    url(r'^updateById/', updateById),
    url(r'^checkcommunication/', check),

]