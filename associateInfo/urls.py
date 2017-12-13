from django.conf.urls import url
from associateInfo.views import *

urlpatterns = [
    url(r'^addOne/', addOne),
    url(r'^findOneById/', findOneById),
    # url(r'^findMembersByOrganizeid/',findMembersByOrganizeid),
    url(r'^updateIdentityById/',updateIdentityById),
    url(r'^updateStateById/',updateStateById),
    url(r'^findMembersByOrganizeDepartid/',findMembersByOrganizeDepartid),
    url(r'^findMemberByIdentityForChangeChairman/',findMemberByIdentityForChangeChairman),
    url(r'^deleteById/',deleteById),
]