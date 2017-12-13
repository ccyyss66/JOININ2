from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from department.models import *
from django.http import *

# Create your views here.
@csrf_exempt
def addOne(request):
    departmentDic = json.loads(str(request.body, encoding="utf-8"))["department"]
    department = Department.objects.get_or_create(name=departmentDic["name"], schoolid=departmentDic["schoolid"], universityid=departmentDic["universityid"])
    if department[1]==False:
        return JsonResponse({"message": "系已存在", "success": False})
    else:
        return JsonResponse({"message": "创建系成功", "success": True})

@csrf_exempt  #通过学院id查找系部
def findBySchoolId(request):
    deparmentListDict = []
    schoolid = json.loads(str(request.body, encoding="utf-8"))["id"]
    departmentList = Department.objects.filter(schoolid=schoolid).order_by('name')
    for department in departmentList:
        deparmentListDict.append(department.dict())
    return JsonResponse({"message": "查找成功", "success": True, "data": deparmentListDict})