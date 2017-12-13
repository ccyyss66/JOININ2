from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from communication.models import *
from image.models import *
from django.contrib.auth.models import User
from school.models import *
# Create your views here.

@csrf_exempt
def addOne(request):
    communication = json.loads(str(request.body, encoding="utf-8"))["communication"]
    communication.pop("csrfmiddlewaretoken")
    Communication.objects.create(**communication)
    return JsonResponse({"message": "添加成功", "success":True})


@csrf_exempt #返回一条信息记录和图片信息
def findOneDetailById(request):
    id = json.loads(str(request.body, encoding="utf-8"))["id"]
    try:
        communication = Communication.objects.get(id=id)
        if communication.activity!='' and communication.activity!=0 and communication.activity!=None:
            image = Image.objects.get(id=communication.activity)
            image.path = settings.MEDIA_ROOT + image.path
            image = image.dict()
        else:
            image = None
        if communication.schoolid!='' and communication.schoolid!=0 and communication.schoolid!=None:
            school = School.objects.get(id=communication.schoolid).dict()
        else:
            school = None
        if communication.userid!='' and communication.userid!=0 and communication.userid!=None:
            publisher = User.objects.get(id=communication.userid).__dict__
            publisher.pop('_state')
            publisher.pop('password')
        else:
            publisher = None
        return JsonResponse({"message": "查找成功", "communication": communication.dict(), "image": image,"school":school,"publisher":publisher, "success": True})
    except:
        return JsonResponse({"message": "查找失败", "success": False})


@csrf_exempt
def findListByUserId(request):
    userid = json.loads(str(request.body, encoding="utf-8"))["userid"]
    communicationList = []
    try:
        communications = Communication.objects.filter(userid=userid).order_by('start')
        for communication in communications:
            communicationDetail = {"communication":"", "image":""}
            image = ""
            if communication.activity != '' and communication.activity != 0 and communication.activity !=None :
                image = Image.objects.get(id=communication.activity)
                image.path = settings.MEDIA_ROOT + image.path
            communicationDetail["communication"] = communication.dict()
            if image != None and image != '':
                communicationDetail["image"] = image.dict()
            communicationList.append(communicationDetail)
        return JsonResponse({"message": "查找成功", "success": True, "data": communicationList, "total":communicationList.__len__()})
    except:
        return JsonResponse({"message": "查找失败", "success": False})


@csrf_exempt
def findByCondition(request):
    userid = json.loads(str(request.body, encoding="utf-8"))["userid"]
    state = json.loads(str(request.body, encoding="utf-8"))["state"]
    schoolid = json.loads(str(request.body, encoding="utf-8"))["schoolid"]
    communicationList = []
    communicationQuerySet = Communication.objects.all()
    if userid != None and userid != '':
        communicationQuerySet = communicationQuerySet.filter(userid=userid)
    if state != None and state != '':
        communicationQuerySet = communicationQuerySet.filter(state=state)
    if schoolid != None and schoolid != '':
        communicationQuerySet = communicationQuerySet.filter(schoolid=schoolid)
    for communication in communicationQuerySet:
        communicationDetail = {"communication": "", "image": "", "publisher": "", "school": ""}
        image = ""
        communicationDetail["communication"] = communication.dict()
        if communication.activity != '' and communication.activity != 0 and communication.activity != None:
            image = Image.objects.get(id=communication.activity)
            image.path = settings.MEDIA_ROOT + image.path
        if image != None and image != '':
            communicationDetail["image"] = image.dict()
        if communication.userid != '' and communication.userid != 0 and communication.userid != None:
            publisher = User.objects.get(id=communication.userid).__dict__
            publisher.pop('_state')
            publisher.pop('password')
            communicationDetail["publisher"] = publisher
        if communication.schoolid != '' and communication.schoolid != 0 and communication.schoolid != None:
            communicationDetail["school"] = School.objects.get(id=communication.schoolid).dict()
        communicationList.append(communicationDetail)
    return JsonResponse({"message": "查找成功", "success": True, "data": communicationList, "total": communicationList.__len__()})


@csrf_exempt
def deleteById(request):
    id = json.loads(str(request.body, encoding="utf-8"))["id"]
    try:
        communication = Communication.objects.filter(id=id)
        if communication.activity != None and communication.activity != '' and communication.activity != 0:
            Image.objects.filter(id=communication.activity).delete()
        communication.delete()
        return JsonResponse({"message": "删除成功", "success": True})
    except:
        return JsonResponse({"message": "删除失败，请重试", "success": False})


@csrf_exempt
def updateById(request):
    communication = json.loads(str(request.body, encoding="utf-8"))["communication"]
    communication.pop("csrfmiddlewaretoken")
    oldCommunication = Communication.objects.get(id=communication["id"])
    if oldCommunication.schoolid!=communication["schoolid"]:
        oldCommunication.schoolid = int(communication["schoolid"])
    if oldCommunication.topic!=communication["topic"]:
        oldCommunication.topic = communication["topic"]
    if oldCommunication.start != communication["start"]:
        oldCommunication.start = communication["start"]
    if oldCommunication.end != communication["end"]:
        oldCommunication.end = communication["end"]
    if communication["activity"]!=None and oldCommunication.activity != communication["activity"] and communication["activity"]!='':
        oldCommunication.activity = int(communication["activity"])
    if oldCommunication.qq != communication["qq"]:
        oldCommunication.qq = communication["qq"]
    if oldCommunication.wechat != communication["wechat"]:
        oldCommunication.wechat = communication["wechat"]
    if oldCommunication.phone != communication["phone"]:
        oldCommunication.phone = communication["phone"]
    if communication["state"] != None and oldCommunication.state != communication["state"]:
        oldCommunication.state = communication["state"]
    if communication["content"] != None and oldCommunication.content!=communication["content"]:
        oldCommunication.content = communication["content"]
    try:
        oldCommunication.save()
        return JsonResponse({"message": "修改成功", "success": True})
    except:
        return JsonResponse({"message": "修改失败，请重试", "success": False})




@csrf_exempt
def check(request):
    id = json.loads(str(request.body, encoding="utf-8"))["id"]
    print(id)
    state = json.loads(str(request.body, encoding="utf-8"))["state"]
    print(state)
    communication = Communication.objects.get(id=id)
    communication.state = state
    try:
        communication.save();
        return  JsonResponse({"message": "审核成功", "success": True})
    except:
        return JsonResponse({"message": "审核失败，请重试", "success": False})
