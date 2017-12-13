from django.conf.urls import url
from image.views import *

urlpatterns = [
    url(r'^findOneById/',findOneById),
    url(r'^upload/',upload),
    # url(r'^/',),
]