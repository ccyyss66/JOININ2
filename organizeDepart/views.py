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
# Create your views here.

@csrf_exempt
def addOne(request):
    organizeDepartDic = json.loads(str(request.body, encoding="utf-8"))["organizeDepart"]
    organizeDepart = OrganizeDepart.objects.get_or_create(**organizeDepartDic)
    if organizeDepart[1] == False:
        return JsonResponse({"message": "该部门已存在", "success": False})
    else:
        return JsonResponse({"message": "添加成功", "success": True})

@csrf_exempt
def deleteOneById(request):
    organizeDepartid = json.loads(str(request.body, encoding="utf-8"))["id"]
    try:
        OrganizeDepart.objects.get(id=organizeDepartid).delete()
        return JsonResponse({"success":True,"message":"删除成功"})
    except:
        return JsonResponse({"success":False,"message":"删除失败"})

@csrf_exempt
def findByOrganizeid(request):
    organizeid = json.loads(str(request.body, encoding="utf-8"))["organizeid"]
    organizeDepartList = []

    # 以下三行用于检验是否已加入该组织
    session_userId = request.session.get('userId')
    try:
        stinfo = StudentInfo.objects.get(userid=session_userId)
        isJoininThisOraganize = checkIsJoinIn(stinfo.id, organizeid)
    except:
        isJoininThisOraganize = ""

    organizeDepartQuerySet = OrganizeDepart.objects.filter(organizeid=organizeid)
    for organizeDepart in organizeDepartQuerySet:
        organizeDepartDetail = {"organizeDepart":organizeDepart.dict(),"isJoininThisOraganize":isJoininThisOraganize}
        organizeDepartList.append(organizeDepartDetail)
    return JsonResponse({"success":True,"message":"查找成功","data":organizeDepartList,"total":organizeDepartList.__len__()})

def checkIsJoinIn(stid,organizedid):
    if AssociateInfo.objects.filter(sno=stid, organizeid=organizedid):
        return AssociateInfo.objects.get(sno=stid, organizeid=organizedid).state
    else:
        return False