from django.db import models
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from image.models import *
import os
import json
import time as tim
from django.conf import settings
from PIL import Image as imag
# Create your views here.

@csrf_exempt
def findOneById(request):
    id = json.loads(str(request.body, encoding="utf-8"))["id"]
    try:
        img = Image.objects.get(id=id)
        path = os.path.join(settings.MEDIA_ROOT,img.path)
        if os.path.exists(path):
            img.path = settings.MEDIA_ROOT+path
            return JsonResponse({"data": img.dict(), "message": "查找成功"})
        else:
            return JsonResponse({"data": None,"message": "图片文件不存在", "success": False})
    except:
        return JsonResponse({"data":None, "message": "图片不存在", "success": False})


@csrf_exempt
def upload(request):
    file = request.FILES.get("fileUp")
    time = tim.time()
    fileType = file.__str__().split(".")[-1]
    filename = time.__str__()+"."+fileType
    path = os.path.join(settings.MEDIA_ROOT,'upload/'+filename)
    file = imag.open(file).convert('RGB')
    file.save(path)
    Img = Image()
    Img.path = filename
    Img.description = '活动图片'
    Img.name = '活动地点图片'
    # Img.save()
    img = Image.objects.get_or_create(path=Img.path,description=Img.description,name=Img.name)
    if img[1]:
        return JsonResponse({"success": True, "message": "上传图片成功", "data": img[0].dict()})
    else:
        return JsonResponse({"success":False, "message":"上传失败，请重试"})