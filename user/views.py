from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password

from django.contrib.auth.models import User
from student.models import *
from associateInfo.models import *
from schoolAdmin.models import *
# Create your views here.
def register(request):
    return render(request,"register.html")

def userlogin(request):
    return render(request,"userlogin.html")

def logout(request):
    if request.session.get('userId'):
        del request.session["userId"]
    return render(request, "userlogin.html")

@csrf_exempt
def userRegister(request):
    userDict = json.loads(str(request.body, encoding="utf-8"))["newUser"]
    try:
        User.objects.get(username=userDict["username"])
        isUser = 1
    except:
        isUser = 0  #用来判断用户名是否存在 0为不存在

    if isUser == 1:
        return JsonResponse({"message": "该用户名已存在", "success": False})
    else:
        userDict.pop("csrfmiddlewaretoken")
        userDict.pop("repassword")
        userDict["password"] = make_password(userDict["password"])
        print(userDict)
        user = User.objects.create(**userDict)
        StudentInfo.objects.create(userid=user.id,universityid=1) #创建该用户的学生信息表
        return JsonResponse({"message": "创建用户成功", "success": True,"url":"/user/userlogin"})

@csrf_exempt
def login(request):
    userDict = json.loads(str(request.body, encoding="utf-8"))["user"]
    user = User.objects.get(username=userDict["username"])
    if check_password(userDict["password"], user.password):
        request.session["userId"] = user.id
        if user.is_staff == 0 and user.is_superuser==0:
            return JsonResponse({"message": "/student/studentIndex", "success": True})
        elif user.is_staff == 1 and user.is_superuser == 1:
            return JsonResponse({"message": "/system/index", "success": True})
        elif user.is_staff == 1 and user.is_superuser == 0:
            return JsonResponse({"message": "/schoolAdmin/index", "success": True})
    else:
        return JsonResponse({"message": "密码错误", "success": False})

@csrf_exempt
def addOneChairman(request):
    userDict = json.loads(str(request.body, encoding="utf-8"))["newUser"]
    asso = json.loads(str(request.body, encoding="utf-8"))["associateInfo"]
    try:
        User.objects.get(username=userDict["username"])
        isUser = 1
    except:
        isUser = 0  #用来判断用户名是否存在 0为不存在

    if isUser == 1:
        return JsonResponse({"message": "该用户名已存在", "success": False})
    else:
        user = User.objects.create(username=userDict["username"], password=make_password(userDict["password"]), is_staff=userDict["is_staff"],last_name=userDict["last_name"])
        studentInfo = StudentInfo.objects.create(userid=user.id,universityid=1)
        AssociateInfo.objects.create(sno=studentInfo.id,identity=1,organizeid=asso["organizeid"],organizedepartid=-1,state=2)
        return JsonResponse({"message": "创建用户成功", "success": True})


@csrf_exempt
def findOneDetailById(request):
    id = json.loads(str(request.body, encoding="utf-8"))["userid"]
    user = User.objects.get(id=id)
    schoolAdmin = SchoolAdmin.objects.get(userid=id)
    user=user.__dict__
    user.pop('_state')
    user.pop('password')
    return JsonResponse({"message": "查找成功", "success": True,"user":user,"schoolAdmin":schoolAdmin.dict()})