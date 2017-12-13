from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from school.models import *
from schoolAdmin.models import *
from django.contrib.auth.models import User
from university.models import *
from organize.models import *
from associateInfo.models import *
from student.models import *

# Create your views here.
@csrf_exempt
def addOne(request):
    organizeDic = json.loads(str(request.body, encoding="utf-8"))["organize"]
    # organizeDic.pop("csrfmiddlewaretoken")
    organize = Organize.objects.get_or_create(**organizeDic)
    if organize[1] == False:
        return JsonResponse({"message": "该组织已存在", "success": False})
    else:
        return JsonResponse({"message": "添加成功", "success": True})

@csrf_exempt
def findOneDetailById(request):
    id = json.loads(str(request.body, encoding="utf-8"))["id"]
    try:
        organize = Organize.objects.get(id=id)
        university = ""
        school = ""
        if organize.universityid!=None and organize.universityid != '':
            university = University.objects.get(id=organize.universityid).dict()
        if organize.schoolid!=None and organize.schoolid != '' and organize.schoolid!=-1:
            school = School.objects.get(id=organize.schoolid).dict()
        return JsonResponse({"message": "查找成功", "success": True, "organize":organize.dict(), "university": university, "school": school})
    except:
        return JsonResponse({"message": "查询失败", "success": False})


@csrf_exempt
def findByCondition(request):
    universityid = json.loads(str(request.body, encoding="utf-8"))["universityid"]
    schoolid = json.loads(str(request.body, encoding="utf-8"))["schoolid"]
    organizeList = []
    organizeQuerySet = Organize.objects.all()
    if universityid != None and universityid != '':
        organizeQuerySet = organizeQuerySet.filter(universityid=universityid)
    if schoolid != None and schoolid != '':
        organizeQuerySet = organizeQuerySet.filter(schoolid=schoolid)
    for organize in organizeQuerySet:
        organizeDetail = {"organize": "", "university": "", "school": "","chairmanUser":"","chairmanStudentInfo":""}
        organizeDetail["organize"] = organize.dict()
        if organize.universityid != '' and organize.universityid != 0 and organize.universityid != None:
            organizeDetail["university"] = University.objects.get(id=organize.universityid).dict()
        if organize.schoolid != '' and organize.schoolid != 0 and organize.schoolid != None and organize.schoolid != -1:
            organizeDetail["school"] = School.objects.get(id=organize.schoolid).dict()
        try:
            chairman = AssociateInfo.objects.get(organizeid=organize.id,identity=1)
            chairmanStudentInfo = StudentInfo.objects.get(id=chairman.sno)
            chairmanUser = User.objects.get(id=chairmanStudentInfo.userid).__dict__
            chairmanUser.pop('_state')
            chairmanUser.pop('password')
            organizeDetail["chairmanUser"] = chairmanUser
            organizeDetail["chairmanStudentInfo"] = chairmanStudentInfo.dict()
        except:
            organizeDetail["chairmanUser"] = ""
        organizeList.append(organizeDetail)
    return JsonResponse({"message": "查找成功", "success": True, "data": organizeList, "total": organizeList.__len__()})

@csrf_exempt
def findByConditionBySt(request):
    universityid = json.loads(str(request.body, encoding="utf-8"))["universityid"]
    schoolid = json.loads(str(request.body, encoding="utf-8"))["schoolid"]
    session_userId = request.session.get('userId')
    stinfo = StudentInfo.objects.get(userid=session_userId)
    organizeList = []
    organizeQuerySet = Organize.objects.all()
    if universityid != None and universityid != '':
        organizeQuerySet = organizeQuerySet.filter(universityid=universityid)
    if schoolid != None and schoolid != '':
        organizeQuerySet = organizeQuerySet.filter(schoolid=schoolid)
    for organize in organizeQuerySet:
        organizeDetail = {"organize": "", "university": "", "school": "" ,"isJoinin":""}
        organizeDetail["organize"] = organize.dict()
        if organize.universityid != '' and organize.universityid != 0 and organize.universityid != None:
            organizeDetail["university"] = University.objects.get(id=organize.universityid).dict()
        if organize.schoolid != '' and organize.schoolid != 0 and organize.schoolid != None and organize.schoolid != -1:
            organizeDetail["school"] = School.objects.get(id=organize.schoolid).dict()
        organizeDetail["isJoinin"] = checkIsJoinIn(stinfo.id,organize.id)
        organizeList.append(organizeDetail)
    return JsonResponse({"message": "查找成功", "success": True, "data": organizeList, "total": organizeList.__len__()})

@csrf_exempt
def modifyOneById(request):
    oldOrganize = json.loads(str(request.body,encoding="utf-8"))["organize"]
    organize = Organize.objects.get(id=oldOrganize["id"])
    try:
        organize.name = oldOrganize["name"]
        organize.introduce =oldOrganize["intro"]
        organize.save()
        return JsonResponse({"message":"修改成功","success":True})
    except:
        return JsonResponse({"message":"修改失败","success":False})


@csrf_exempt
def deleteOneById(request):
    id = json.loads(str(request.body,encoding="utf-8"))["id"]
    try:
        Organize.objects.filter(id=id).delete()
        AssociateInfo.objects.filter(organizeid=id).delete()
        return JsonResponse({"message":"删除成功","success":True})
    except:
        return JsonResponse({"message":"删除失败","success":False})



def checkIsJoinIn(stid,organizedid):
    if AssociateInfo.objects.filter(sno=stid, organizeid=organizedid):
        return True
    else:
        return False


