from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from school.models import *
from department.models import *
from major.models import *
from clazz.models import *
from schoolAdmin.models import *
from django.contrib.auth.models import User
from university.models import *
from organize.models import *
from organizeDepart.models import *
from associateInfo.models import *
from student.models import *

@csrf_exempt
def addOne(request):
    associateInfoDic = json.loads(str(request.body, encoding="utf-8"))["associateInfo"]
    associateInfo = AssociateInfo.objects.get_or_create(**associateInfoDic)
    if associateInfo[1] == False:
        return JsonResponse({"message": "该成员已存在", "success": False})
    else:
        return JsonResponse({"message": "添加成功", "success": True})


@csrf_exempt
def findOneById(request):
    id = json.loads(str(request.body, encoding="utf-8"))["id"]
    try:
        associateInfo = AssociateInfo.objects.get(id=id)
        return JsonResponse({"message": "查找成功", "success": True, "data":associateInfo.dict()})
    except:
        return JsonResponse({"message": "查询失败", "success": False})


# @csrf_exempt
# def findMembersByOrganizeid(request):
#     organizeid = json.loads(str(request.body, encoding="utf-8"))["organizeid"]
#     state = json.loads(str(request.body, encoding="utf-8"))["state"]
#     memberList = []
#     associateInfoQuerySet = AssociateInfo.objects.filter(organizeid=organizeid,state=state)
#     for associateInfo in associateInfoQuerySet:
#         memberDetail = {"user":"", "studentInfo":"","school":"","department":"","major":"","clazz":"","associateInfo":associateInfo.dict()}
#         studentInfo = StudentInfo.objects.get(id=associateInfo.sno)
#         memberDetail["studentInfo"] = studentInfo.dict()
#         memberDetail["user"] = User.objects.get(id=studentInfo.userid).dict()
#         if studentInfo.classid!=None:
#             memberDetail["school"] = School.objects.get(id=studentInfo.schoolid).dict()
#             memberDetail["department"] = Department.objects.get(id=studentInfo.departmentid).dict()
#             memberDetail["major"] = Major.objects.get(id=studentInfo.majorid).dict()
#             memberDetail["clazz"] = Clazz.objects.get(id=studentInfo.classid).dict()
#         memberList.append(memberDetail)
#     return JsonResponse({"success":True, "data":memberList, "message":"查找成功"})

@csrf_exempt
def findMembersByOrganizeDepartid(request):
    organizeDepartid = json.loads(str(request.body, encoding="utf-8"))["organizeDepartid"]
    organizeid = json.loads(str(request.body, encoding="utf-8"))["organizeid"]
    memberList = []
    # 用于判断在该组织的身份
    session_userId = request.session.get('userId')
    try:
        stinfo = StudentInfo.objects.get(userid=session_userId)
        asso = AssociateInfo.objects.get(sno=stinfo.id,organizeid=organizeid)
        currentUserIdentity = asso.identity
    except:
        currentUserIdentity = ""

    associateInfoQuerySet = AssociateInfo.objects.filter(organizedepartid=organizeDepartid).exclude(state=3)
    for associateInfo in associateInfoQuerySet:
        memberDetail = {"user":"", "studentInfo":"","school":"","department":"","major":"","clazz":"","associateInfo":associateInfo.dict(),"currentUserIdentity":currentUserIdentity}
        studentInfo = StudentInfo.objects.get(id=associateInfo.sno)
        memberDetail["studentInfo"] = studentInfo.dict()
        user = User.objects.get(id=studentInfo.userid).__dict__
        user.pop('_state')
        user.pop('password')
        memberDetail["user"] = user
        if studentInfo.classid!=None:
            memberDetail["school"] = School.objects.get(id=studentInfo.schoolid).dict()
            memberDetail["department"] = Department.objects.get(id=studentInfo.departmentid).dict()
            memberDetail["major"] = Major.objects.get(id=studentInfo.majorid).dict()
            memberDetail["clazz"] = Clazz.objects.get(id=studentInfo.classid).dict()
        memberList.append(memberDetail)
    return JsonResponse({"success":True, "data":memberList, "message":"查找成功","total":memberList.__len__()})

@csrf_exempt
def findMemberByIdentityForChangeChairman(request):
    organizeid = json.loads(str(request.body, encoding="utf-8"))["organizeid"]
    identity = json.loads(str(request.body, encoding="utf-8"))["identity"]
    memberQuerySet = AssociateInfo.objects.filter(organizeid=organizeid,identity=identity)
    memberlist = []
    for member in memberQuerySet:
        memberDetail = {"user":"","depart":"","studentInfo":"","associateInfo":member.dict()}
        memberDetail["depart"] = OrganizeDepart.objects.get(id=member.organizedepartid).dict()
        studentInfo = StudentInfo.objects.get(id=member.sno)
        memberDetail["studentInfo"] = studentInfo.dict()
        user=User.objects.get(id=studentInfo.userid).__dict__
        user.pop('_state')
        user.pop('password')
        memberDetail["user"] = user
        memberlist.append(memberDetail)
    return JsonResponse({"success":True,"message":"查找成功","data":memberlist,"total":memberlist.__len__()})

@csrf_exempt
def updateIdentityById(request):
    id = json.loads(str(request.body, encoding="utf-8"))["id"]
    identity = json.loads(str(request.body, encoding="utf-8"))["identity"]
    try:
        associateInfo = AssociateInfo.objects.get(id=id)
        associateInfo.identity = identity
        associateInfo.save()
        return JsonResponse({"success":True,"message":"修改成功"})
    except:
        return JsonResponse({"success":False,"message":"修改失败"})

@csrf_exempt
def updateStateById(request):
    id = json.loads(str(request.body, encoding="utf-8"))["id"]
    state = json.loads(str(request.body, encoding="utf-8"))["state"]
    try:
        associateInfo = AssociateInfo.objects.get(id=id)
        associateInfo.state = state
        associateInfo.identity = 4
        associateInfo.save()
        return JsonResponse({"success":True,"message":"修改成功"})
    except:
        return JsonResponse({"success":False,"message":"修改失败"})

@csrf_exempt
def deleteById(request):
    id = json.loads(str(request.body, encoding="utf-8"))["id"]
    try:
        AssociateInfo.objects.get(id=id).delete()
        return JsonResponse({"success":True,"message":"删除成功"})
    except:
        return JsonResponse({"success":False,"message":"删除失败"})