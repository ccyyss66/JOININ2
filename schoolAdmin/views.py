from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from schoolAdmin.models import *
from department.models import *
from major.models import *
from clazz.models import *
# Create your views here.
def index(request):
    session_userId = request.session.get('userId')
    return render(request,"schoolAdmin/index.html",{"session_userId":session_userId})

def personalInfo(request):
    session_userId = request.session.get('userId')
    return render(request,"schoolAdmin/personalInfo.html",{"session_userId":session_userId})

def addDepartment(request):
    session_userId = request.session.get('userId')
    return render(request,"schoolAdmin/addDepartment.html",{"session_userId":session_userId})

def addMajor(request):
    session_userId = request.session.get('userId')
    return render(request, "schoolAdmin/addMajor.html", {"session_userId": session_userId})

def addClass(request):
    session_userId = request.session.get('userId')
    return render(request, "schoolAdmin/addClass.html", {"session_userId": session_userId})

def departmentAndMajorAndClass(request):
    session_userId = request.session.get('userId')
    return render(request,"schoolAdmin/departmentAndMajorAndClass.html",{"session_userId":session_userId})

def communication(request):
    session_userId = request.session.get('userId')
    return render(request,"schoolAdmin/communication.html", {"session_userId":session_userId})

def organized(request):
    session_userId = request.session.get('userId')
    return render(request,"schoolAdmin/organized.html",{"session_userId":session_userId})

def viewmates(request,departId):
    return render(request,"schoolAdmin/viewMates.html",{"depart_id":departId})

def depart(request,organizeId):
    return render(request,"schoolAdmin/depart.html",{"organized_id":organizeId})

@csrf_exempt
def findSchoolAdminDetailById(request):
    id = json.loads(str(request.body,encoding="utf-8"))["userid"]
    user = User.objects.get(id=id).__dict__
    user.pop('_state')
    user.pop('password')
    schoolAdmin = SchoolAdmin.objects.get(userid=id)
    return JsonResponse({"message": "查找成功", "success": True, "user": user, "schoolAdmin": schoolAdmin.dict()})

@csrf_exempt
def findDepartmentMajorClassDetailBySchoolId(request):
    schoolid = json.loads(str(request.body, encoding="utf-8"))["schoolid"]
    departmentList = Department.objects.filter(schoolid=schoolid).order_by('name')
    classList = []
    if departmentList.__len__() == 0:
        return JsonResponse({"message": "暂无任何系专业班级", "data": "", "success": False})
    else:
        for department in departmentList:
            majorList = Major.objects.filter(departmentid=department.id).order_by('name')
            if majorList.__len__() == 0:
                print("暂无专业")
                classDetail = {}
                classDetail["department"] = department.dict()
                classDetail["major"] = ""
                classDetail["clazz"] = ""
                classList.append(classDetail)
            else:
                for major in majorList:
                    print(major.id)
                    clazzList = Clazz.objects.filter(majorid=major.id).order_by('name')
                    if clazzList.__len__() == 0:
                        print("暂无班级")
                        classDetail = {}
                        classDetail["department"] = department.dict()
                        classDetail["major"] = major.dict()
                        classDetail["clazz"] = ""
                        classList.append(classDetail)
                    else:
                        for clazz in clazzList:
                            print(clazz.name)
                            classDetail = {}
                            classDetail["department"] = department.dict()
                            classDetail["major"] = major.dict()
                            classDetail["clazz"] = clazz.dict()
                            classList.append(classDetail)
        return JsonResponse({"message": "查找成功", "data": classList, "success": True, "total":classList.__len__()})

@csrf_exempt
def addOneSchoolAdmin(request):
    userDict = json.loads(str(request.body, encoding="utf-8"))["user"]
    schoolAdmin = json.loads(str(request.body, encoding="utf-8"))["schoolmanagerinfo"]
    try:
        User.objects.get(username=userDict["username"])
        isUser = 1
    except:
        isUser = 0  #用来判断用户名是否存在 0为不存在

    if isUser == 1:
        return JsonResponse({"message": "该用户名已存在", "success": False})
    else:
        print(userDict)
        user = User.objects.create(username=userDict["username"], password=make_password(userDict["password"]),is_staff=userDict["is_staff"], last_name=userDict["last_name"])
        SchoolAdmin.objects.create(userid=user.id, universityid=1,schoolid=schoolAdmin["schoolid"])
        return JsonResponse({"message": "创建用户成功", "success": True})




