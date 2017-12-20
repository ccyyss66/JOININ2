from django.shortcuts import render
from university.models import *
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def add(request):
    university = json.loads(str(request.body, encoding="utf-8"))["university"]
    uni = University.objects.get_or_create(**university)
    if uni[1]:
        return JsonResponse({"success":True,"message":"初始化成功"})
    else:
        return JsonResponse({"success":False,"message":"已存在"})
