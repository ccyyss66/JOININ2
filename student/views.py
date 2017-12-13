from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from student.models import *
from school.models import *
from department.models import *
from major.models import *
from clazz.models import *

# Create your views here.
def studentIndex(request):
    session_userId = request.session.get('userId')
    return render(request,"student/studentIndex.html",{"session_userId":session_userId})

def personalInfo(request):
    session_userId = request.session.get('userId')
    return render(request,"student/personalInfo.html",{"session_userId":session_userId})

def viewinformation(request):
    session_userId = request.session.get('userId')
    return render(request,"student/viewinformation.html",{"session_userId":session_userId})

def publishinformation(request):
    session_userId = request.session.get('userId')
    return render(request,"student/publishinformation.html",{"session_userId":session_userId})

def associateinfo(request):
    session_userId = request.session.get('userId')
    return render(request,"student/associateInfo.html",{"session_userId":session_userId})

def addInformation(request):
    session_userId = request.session.get('userId')
    communication_id = request.GET.get('communicationid')
    if communication_id==None or communication_id=='':
        communication_id = 'null'
    return render(request,"student/addInformation.html",{"session_userId":session_userId,"communication_id":communication_id})

@csrf_exempt
def findStudentInfoDetailByUserId(request):
    userId = json.loads(str(request.body, encoding="utf-8"))["userId"]
    school = {}
    department = {}
    major = {}
    clazz = {}
    user = User.objects.get(id=userId)
    studentInfo = StudentInfo.objects.get(userid=userId)
    try:
        school = School.objects.get(id=studentInfo.schoolid).dict()
        try:
            department = Department.objects.get(id=studentInfo.departmentid).dict()
            try:
                major = Major.objects.get(id=studentInfo.majorid).dict()
                try:
                    clazz = Clazz.objects.get(id=studentInfo.classid).dict()
                except:
                    clazz = ""
            except:
                major = ""
        except:
            department = ""
    except:
        school = ""
    user = user.__dict__
    user.pop('_state')
    user.pop('password')
    studentInfo = studentInfo.dict()
    return JsonResponse({"message": "查找成功", "success": True,"studentInfo":studentInfo,"user":user,"school":school,"department":department,"major":major,"clazz":clazz})

@csrf_exempt
def modifyStudentInfoDetail(request):
    newuser = json.loads(str(request.body, encoding="utf-8"))["user"]
    newstudentInfo = json.loads(str(request.body, encoding="utf-8"))["studentinfo"]
    user = User.objects.get(id=newuser["id"])
    studentInfo = StudentInfo.objects.get(userid=newuser["id"])
    try:
        if newuser["email"]!='':
            user.email = newuser["email"]
        if newstudentInfo["mobilephone"]!='':
            studentInfo.mobilephone = newstudentInfo["mobilephone"]
        if newstudentInfo["sex"]!='':
            studentInfo.sex = newstudentInfo["sex"]
        if newuser["last_name"]!='':
            user.last_name = newuser["last_name"]
        if newstudentInfo["qq"] != '':
            studentInfo.qq = newstudentInfo["qq"]
        if newstudentInfo["wechat"]!='':
            studentInfo.wechat = newstudentInfo["wechat"]
        if newstudentInfo["workid"]!='':
            studentInfo.workid = newstudentInfo["workid"]
        if newstudentInfo["universityid"]!='':
            studentInfo.universityid = newstudentInfo["universityid"]
        if newstudentInfo["schoolid"] != '':
            studentInfo.schoolid = newstudentInfo["schoolid"]
        if newstudentInfo["departmentid"] != '':
            studentInfo.departmentid = newstudentInfo["departmentid"]
        if newstudentInfo["majorid"] != '':
            studentInfo.majorid = newstudentInfo["majorid"]
        if newstudentInfo["classid"] != '':
            studentInfo.classid = newstudentInfo["classid"]
        if newstudentInfo["interest"] != '':
            studentInfo.interest = newstudentInfo["interest"]
        user.save()
        studentInfo.save()
        return JsonResponse({"success":True, "message":"修改成功"})
    except:
        return JsonResponse({"success":False, "message":"我也没办法了，后台太简单，自己凑数据吧"})