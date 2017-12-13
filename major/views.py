from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from major.models import *
from django.http import *

# Create your views here.
@csrf_exempt
def addOne(request):
    majorDic = json.loads(str(request.body, encoding="utf-8"))["major"]
    major = Major.objects.get_or_create(name=majorDic["name"], departmentid=majorDic["departmentid"], schoolid=majorDic["schoolid"], universityid=majorDic["universityid"])
    if major[1] == False:
        return JsonResponse({"message": "专业已存在", "success": False})
    else:
        return JsonResponse({"message": "创建专业成功", "success": True})

@csrf_exempt  #通过系部id查找专业
def findByDepartmentId(request):
    majorListDict = []
    departmentid = json.loads(str(request.body, encoding="utf-8"))["id"]
    majorList = Major.objects.filter(departmentid=departmentid).order_by('name')
    for major in majorList:
        majorListDict.append(major.dict())
    return JsonResponse({"message": "查找成功", "success": True, "data": majorListDict})