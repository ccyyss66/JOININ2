from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from school.models import *
from django.core import serializers
from schoolAdmin.models import *
from django.contrib.auth.models import User
from django.http import *
# Create your views here.

class SchoolWithAdminDetail(models.Model):
    user = User
    schoolAdmin = SchoolAdmin
    school = School

    def dict(self):
        user = self.user.__dict__
        user.pop('_state')
        user.pop('password')
        schoolDetail = {
            "schoolAdmin":self.schoolAdmin.dict(),
            "school":self.school.dict(),
            "user":user
        }
        return schoolDetail

@csrf_exempt
def addOne(request):
    schoolDic = json.loads(str(request.body, encoding="utf-8"))["school"]
    school = School.objects.get_or_create(name=schoolDic["name"],universityid=1)
    print(school)
    if school[1] == False:
        return JsonResponse({"message": "学院已存在", "success": False})
    else:
        return JsonResponse({"message": "创建学院成功", "success": True})


@csrf_exempt
def findAllSchool(request):
    schoolList = School.objects.all()
    schoolListDetail = []
    for school in schoolList:
        schoolDetail = {"school":school.dict(),"user":"","schoolAdmin":""}
        try:
            schoolAdmin = SchoolAdmin.objects.get(schoolid=school.id)
            user = User.objects.get(id=schoolAdmin.userid).__dict__
        except:
            schoolAdmin = ""
            user= ""
            print("暂无管理员")
        if user!="":
            user.pop('_state')
            user.pop('password')
            schoolDetail["user"] = user
        if schoolAdmin!="":
            schoolDetail["schoolAdmin"] = schoolAdmin.dict()
        schoolListDetail.append(schoolDetail)
    return JsonResponse({"message": "查找成功", "success": True,"data":schoolListDetail, "total":schoolListDetail.__len__()})

@csrf_exempt
def findByUniversityid(request):
    schoolList = []
    universityid = json.loads(str(request.body, encoding="utf-8"))["id"]
    schoolQuerySet = School.objects.filter(universityid=universityid).order_by('name')
    for school in schoolQuerySet:
        schoolList.append(school.dict())
    return JsonResponse({"message": "查找成功", "success": True, "data": schoolList})