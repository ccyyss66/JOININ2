from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from clazz.models import *
from django.http import *
# Create your views here.
@csrf_exempt
def addOne(request):
    classDic = json.loads(str(request.body, encoding="utf-8"))["clazz"]
    clazz = Clazz.objects.get_or_create(name=classDic["name"],majorid=classDic["majorid"], departmentid=classDic["departmentid"], schoolid=classDic["schoolid"], universityid=classDic["universityid"])
    if clazz[1] == False:
        return JsonResponse({"message": "班级已存在", "success": False})
    else:
        return JsonResponse({"message": "创建班级成功", "success": True})

@csrf_exempt
def findByMajorId(request):
    classListDict = []
    majorid = json.loads(str(request.body, encoding="utf-8"))["id"]
    classList = Clazz.objects.filter(majorid=majorid).order_by('name')
    for clazz in classList:
        classListDict.append(clazz.dict())
    return JsonResponse({"message": "查找成功", "success": True, "data": classListDict})